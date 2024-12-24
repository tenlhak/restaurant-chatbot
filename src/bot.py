from typing import Dict, Optional
from transformers import pipeline
from pinecone import Pinecone, ServerlessSpec
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

from src.storage import RestaurantStorage
from src.config import (
    OPENAI_API_KEY, 
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME,
    PINECONE_DIMENSION,
    PINECONE_METRIC,
    PINECONE_CLOUD,
    PINECONE_REGION,
    GPT_MODEL,
    TEMPERATURE,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    SYSTEM_TEMPLATE
)
from src.utils import extract_order_details, extract_reservation_details

class RestaurantBot:
    """Main restaurant chatbot class handling conversations and interactions."""
    
    def __init__(self, menu_path: str):
        """
        Initialize the restaurant chatbot.
        
        Args:
            menu_path: Path to the menu text file
        """
        self.storage = RestaurantStorage()
        self.menu_path = menu_path
        self._setup_knowledge_base()
        self._setup_conversation_chain()
        self.classifier = pipeline("text-classification", 
                                 model="Falconsai/intent_classification")

    def _setup_knowledge_base(self) -> None:
        """Initialize the restaurant's knowledge base in the vector database."""
        # Load and split documents
        loader = TextLoader(self.menu_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(
            chunk_size=CHUNK_SIZE, 
            chunk_overlap=CHUNK_OVERLAP
        )
        docs = text_splitter.split_documents(documents
