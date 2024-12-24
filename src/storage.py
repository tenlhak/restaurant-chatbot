import json
import sqlite3
from datetime import datetime
from typing import Dict, List, Optional

from src.config import DATABASE_PATH

class RestaurantStorage:
    """Handles persistent storage of orders and reservations."""

    def __init__(self, database_path: str = DATABASE_PATH):
        self.database_path = database_path
        self._init_storage()

    def _init_storage(self) -> None:
        """Initialize the storage system and create necessary tables."""
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()

            # Create orders table
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id TEXT PRIMARY KEY,
                customer_ph_no TEXT NOT NULL,
                items TEXT NOT NULL,
                total_price REAL NOT NULL,
                order_time TEXT NOT NULL,
                status TEXT NOT NULL,
                special_instructions TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            ''')

            # Create reservations table
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                reservation_id TEXT PRIMARY KEY,
                customer_name TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                party_size INTEGER NOT NULL,
                status TEXT NOT NULL,
                special_requests TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            ''')

    def add_order(self, 
                 customer_phone: str, 
                 items: List[Dict], 
                 total_price: float,
                 order_time: str, 
                 special_instructions: Optional[str] = None) -> str:
        """
        Add a new order to the database.
        
        Args:
            customer_phone: Customer's phone number
            items: List of ordered items with details
            total_price: Total order price
            order_time: Requested order time
            special_instructions: Any special instructions or dietary restrictions
            
        Returns:
            str: Generated order ID
        """
        order_id = f"ORD{datetime.now().strftime('%Y%m%d%H%M%S')}"

        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO orders (
                order_id, customer_ph_no, items, total_price, 
                order_time, status, special_instructions
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                order_id, 
                customer_phone, 
                json.dumps(items), 
                total_price,
                order_time, 
                "pending", 
                special_instructions
            ))

        return order_id

    def add_reservation(self, 
                       customer_name: str, 
                       date: str, 
                       time: str,
                       party_size: int, 
                       special_requests: Optional[str] = None) -> str:
        """
        Add a new reservation to the database.
        
        Args:
            customer_name: Name of the customer
            date: Reservation date
            time: Reservation time
            party_size: Number of people
            special_requests: Any special requests
            
        Returns:
            str: Generated reservation ID
        """
        reservation_id = f"RES{datetime.now().strftime('%Y%m%d%H%M%S')}"

        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO reservations (
                reservation_id, customer_name, date, time,
                party_size, status, special_requests
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                reservation_id, 
                customer_name, 
                date, 
                time, 
                party_size,
                "confirmed", 
                special_requests
            ))

        return reservation_id

    def get_order(self, order_id: str) -> Optional[Dict]:
        """Retrieve order details by order ID."""
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM orders WHERE order_id = ?', (order_id,))
            order = cursor.fetchone()
            
            if order:
                columns = [description[0] for description in cursor.description]
                return dict(zip(columns, order))
            return None

    def get_reservation(self, reservation_id: str) -> Optional[Dict]:
        """Retrieve reservation details by reservation ID."""
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM reservations WHERE reservation_id = ?', 
                         (reservation_id,))
            reservation = cursor.fetchone()
            
            if reservation:
                columns = [description[0] for description in cursor.description]
                return dict(zip(columns, reservation))
            return None
