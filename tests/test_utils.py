import unittest
from src.utils import validate_phone_number, format_currency

class TestUtils(unittest.TestCase):
    def test_validate_phone_number(self):
        """Test phone number validation."""
        # Valid phone numbers
        self.assertTrue(validate_phone_number("1234567890"))
        self.assertTrue(validate_phone_number("123-456-7890"))
        self.assertTrue(validate_phone_number("(123) 456-7890"))
        
        # Invalid phone numbers
        self.assertFalse(validate_phone_number("123"))
        self.assertFalse(validate_phone_number("abc"))
        self.assertFalse(validate_phone_number("12345678901"))  # Too long

    def test_format_currency(self):
        """Test currency formatting."""
        self.assertEqual(format_currency(10), "$10.00")
        self.assertEqual(format_currency(10.5), "$10.50")
        self.assertEqual(format_currency(10.99), "$10.99")
        self.assertEqual(format_currency(0), "$0.00")
        self.assertEqual(format_currency(1000.999), "$1001.00")

if __name__ == '__main__':
    unittest.main()
