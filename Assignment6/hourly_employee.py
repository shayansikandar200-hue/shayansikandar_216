"""
hourly_employee.py
Hourly employee paid by hours worked.
"""

from employee import Employee


class HourlyEmployee(Employee):
    """
    Hourly employee.
    """

    def __init__(self, name: str, employee_id: int, hourly_rate: float):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def add_hours(self, hours: float):
        """Adds worked hours."""
        self.hours_worked += hours

    def get_pay(self) -> float:
        """Return calculated pay."""
        return self.hours_worked * self.hourly_rate