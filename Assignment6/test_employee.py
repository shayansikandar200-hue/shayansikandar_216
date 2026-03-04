"""
Unit tests for Employee hierarchy.
Runs automatically when executed directly.
"""

import unittest
from manager import Manager
from sales_employee import SalesEmployee
from hourly_employee import HourlyEmployee


class TestEmployees(unittest.TestCase):

    def test_manager_pay(self):
        m = Manager("Alice", 1, 5000)
        self.assertEqual(m.get_pay(), 5000)

    def test_manager_method(self):
        m = Manager("Alice", 1, 5000)
        self.assertEqual(m.approve_budget(), "Budget approved")

    def test_sales_pay(self):
        s = SalesEmployee("Bob", 2, 2000, 500)
        self.assertEqual(s.get_pay(), 2500)

    def test_sales_add_sale(self):
        s = SalesEmployee("Bob", 2, 2000, 0)
        s.add_sale(1000)
        self.assertEqual(s.get_pay(), 2100)

    def test_hourly_pay(self):
        h = HourlyEmployee("Charlie", 3, 20)
        h.add_hours(10)
        self.assertEqual(h.get_pay(), 200)

    def test_info_method(self):
        h = HourlyEmployee("Charlie", 3, 20)
        self.assertIn("Charlie", h.get_info())


if __name__ == "__main__":
    unittest.main()