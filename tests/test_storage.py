import unittest
import os
import json
from src.storage import RestaurantStorage

class TestRestaurantStorage(unittest.TestCase):
    def setUp(self):
        """Set up test database before each test."""
        self.test_db = "test_restaurant.db"
        self.storage = RestaurantStorage(database_path=self.test_db)

    def tearDown(self):
        """Clean up test database after each test."""
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_add_order(self):
        """Test adding a new order."""
        # Test data
        customer_phone = "1234567890"
        items = [
            {"name": "Sushi Roll", "quantity": 2, "price": 15.99},
            {"name": "Miso Soup", "quantity": 1, "price": 4.99}
        ]
        total_price = 36.97
        order_time = "ASAP"
        special_instructions = "No wasabi"

        # Add order
        order_id = self.storage.add_order(
            customer_phone=customer_phone,
            items=items,
            total_price=total_price,
            order_time=order_time,
            special_instructions=special_instructions
        )

        # Verify order was added
        stored_order = self.storage.get_order(order_id)
        self.assertIsNotNone(stored_order)
        self.assertEqual(stored_order['customer_ph_no'], customer_phone)
        self.assertEqual(json.loads(stored_order['items']), items)
        self.assertEqual(stored_order['total_price'], total_price)
        self.assertEqual(stored_order['special_instructions'], special_instructions)

    def test_add_reservation(self):
        """Test adding a new reservation."""
        # Test data
        customer_name = "John Doe"
        date = "2024-12-25"
        time = "18:00"
        party_size = 4
        special_requests = "Window seat preferred"

        # Add reservation
        reservation_id = self.storage.add_reservation(
            customer_name=customer_name,
            date=date,
            time=time,
            party_size=party_size,
            special_requests=special_requests
        )

        # Verify reservation was added
        stored_reservation = self.storage.get_reservation(reservation_id)
        self.assertIsNotNone(stored_reservation)
        self.assertEqual(stored_reservation['customer_name'], customer_name)
        self.assertEqual(stored_reservation['date'], date)
        self.assertEqual(stored_reservation['time'], time)
        self.assertEqual(stored_reservation['party_size'], party_size)
        self.assertEqual(stored_reservation['special_requests'], special_requests)

if __name__ == '__main__':
    unittest.main()
