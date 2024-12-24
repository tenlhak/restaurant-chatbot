"""
Restaurant Chatbot Package

This package provides a conversational AI chatbot for handling restaurant orders and reservations.
"""

from .bot import RestaurantBot
from .storage import RestaurantStorage
from .utils import extract_order_details, extract_reservation_details

__all__ = [
    'RestaurantBot',
    'RestaurantStorage',
    'extract_order_details',
    'extract_reservation_details'
]

__version__ = '0.1.0'
