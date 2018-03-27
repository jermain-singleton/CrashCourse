import unittest
from city_country_function import city_function

class NamesTestCase(unittest.TestCase):
    """Test for city country"""

    def test_city_function(self):
        """Does Miami, USA work"""
        format_name = city_function('Miami', 'U S A')
        self.assertEqual(format_name, 'Miami, U S A')

unittest.main()