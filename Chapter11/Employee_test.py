import unittest
from Employee import Employee_Information

class TestEmployee_Information(unittest.TestCase):
    """Tests for the class Employee_Information"""

    def setUp(self):
        self.myuser = Employee_Information('Germain', 'Singleton', 0)
        

    def test_give_raise(self):
        self.myuser.give_raise()
        self.assertEqual(self.myuser.annual_salary, 5000)
    
    def test_give_custom_raise(self):
        self.myuser.give_raise(25000)
        self.assertEqual(self.myuser.annual_salary, 25000)

        

unittest.main()