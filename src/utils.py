from typing import Dict, List, Optional
from openai import OpenAI
import json

client = OpenAI()

def extract_order_details(conversation_history: List[str]) -> Optional[Dict]:
    """
    Extract order details from conversation history using GPT-4.
    
    Args:
        conversation_history: List of conversation messages
        
    Returns:
        Dict containing order details or None if incomplete
    """
    prompt = f"""
    Based on this conversation, extract the order details in JSON format:
    
    {conversation_history}
    
    Return a JSON object with:
    - phone_number
    - items: list of dictionaries with name, quantity, and price
    - special_instructions (if any dietary restrictions)
    
    If order is not complete, return null.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return None

def extract_reservation_details(conversation_history: List[str]) -> Optional[Dict]:
    """
    Extract reservation details from conversation history using GPT-4.
    
    Args:
        conversation_history: List of conversation messages
        
    Returns:
        Dict containing reservation details or None if incomplete
    """
    prompt = f"""
    Based on this conversation, extract the reservation details in JSON format:
    
    {conversation_history}
    
    Return a JSON object with:
    - name
    - date
    - time
    - party_size
    - special_requests (if any)
    
    If reservation details are not complete, return null.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return None

def validate_phone_number(phone: str) -> bool:
    """
    Validate phone number format.
    
    Args:
        phone: Phone number string
        
    Returns:
        bool: True if valid, False otherwise
    """
    # Remove any non-digit characters
    digits = ''.join(filter(str.isdigit, phone))
    # Check if we have 10 digits
    return len(digits) == 10

def format_currency(amount: float) -> str:
    """
    Format amount as currency string.
    
    Args:
        amount: Float amount
        
    Returns:
        str: Formatted currency string
    """
    return f"${amount:.2f}"
