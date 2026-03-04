"""
sales_employee.py
Sales employee with commission.
"""

from employee import Employee


class SalesEmployee(Employee):
    """
    Sales employee paid base salary + commission.
    """

    def __init__(self, name: str, employee_id: int, base_salary: float, commission: float):
        super().__init__(name, employee_id)
        self.base_salary = base_salary
        self.commission = commission

    def get_pay(self) -> float:
        """Return total pay."""
        return self.base_salary + self.commission

    def add_sale(self, amount: float):
        """Adds commission from sale."""
        self.commission += amount * 0.10