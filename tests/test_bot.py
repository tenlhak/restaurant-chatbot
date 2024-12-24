import unittest
from unittest.mock import patch, MagicMock
from src.bot import RestaurantBot

class TestRestaurantBot(unittest.TestCase):
    @patch('src.bot.PineconeVectorStore')
    @patch('src.bot.Pinecone')
    def setUp(self, mock_pinecone, mock_vectorstore):
        """Set up test environment before each test."""
        # Mock the vector store setup
        self.mock_index = MagicMock()
        mock_pinecone.return_value.list_indexes.return_value.names.return_value = []
        mock_vectorstore.from_documents.return_value = self.mock_index

        # Create bot instance with test menu
        self.bot = RestaurantBot("data/menu.txt")

    def test_handle_message(self):
        """Test basic message handling."""
        # Mock the chain's response
        self.bot.chain.invoke = MagicMock(return_value={'answer': 'Test response'})
        
        # Test message handling
        response = self.bot.handle_message("Hello")
        self.assertEqual(response, "Test response")
        self.bot.chain.invoke.assert_called_once()

    @patch('src.bot.extract_order_details')
    @patch('src.bot.extract_reservation_details')
    def test_process_conversation_outcome(self, mock_extract_reservation, mock_extract_order):
        """Test conversation outcome processing."""
        # Mock successful order
        mock_extract_order.return_value = {
            'phone_number': '1234567890',
            'items': [{'name': 'Sushi', 'quantity': 1, 'price': 10.99}],
            'special_instructions': 'No wasabi'
        }
        
        # Mock successful reservation
        mock_extract_reservation.return_value = {
            'name': 'John Doe',
            'date': '2024-12-25',
            'time': '18:00',
            'party_size': 4,
            'special_requests': 'Window seat'
        }

        # Process outcomes
        result = self.bot.process_conversation_outcome()
        
        # Verify results
        self.assertIsNotNone(result['order_id'])
        self.assertIsNotNone(result['reservation_id'])

if __name__ == '__main__':
    unittest.main()
