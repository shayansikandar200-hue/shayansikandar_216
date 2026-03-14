import unittest

from employee import Employee
from hourly_employee import HourlyEmployee
from commission_employee import CommissionEmployee


class TestEmployees(unittest.TestCase):

    def test_employee_info(self):
        emp = Employee("John", 1)
        self.assertEqual(emp.get_info(), "Employee: John, ID: 1")

    def test_hourly_pay(self):
        emp = HourlyEmployee("Alice", 2, 20)
        emp.add_hours(10)
        self.assertEqual(emp.get_pay(), 200)

    def test_commission_pay(self):
        emp = CommissionEmployee("Bob", 3, 0.1)
        emp.add_sale(1000)
        self.assertEqual(emp.get_pay(), 100)


if __name__ == "__main__":
    unittest.main()