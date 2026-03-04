"""
manager.py
Manager subclass of Employee.
"""

from employee import Employee


class Manager(Employee):
    """
    Manager paid fixed salary.
    """

    def __init__(self, name: str, employee_id: int, salary: float):
        super().__init__(name, employee_id)
        self.salary = salary

    def get_pay(self) -> float:
        """Return monthly salary."""
        return self.salary

    def approve_budget(self) -> str:
        """Unique method for managers."""
        return "Budget approved"