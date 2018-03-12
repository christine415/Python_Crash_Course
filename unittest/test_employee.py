import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def test_give_default_raise(self):
        my_employee = Employee('John', 'Doe', 8000)
        my_employee.give_raise(0)
        self.assertEqual(13000, my_employee.salary)

    def test_give_custom_raise(self):
        my_employee = Employee('John', 'Doe', 8000)
        my_employee.give_raise(10000)
        self.assertEqual(18000, my_employee.salary)

unittest.main()