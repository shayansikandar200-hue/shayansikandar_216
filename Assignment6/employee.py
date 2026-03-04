"""
employee.py
Base Employee class demonstrating inheritance.

Author: Shayan Khan
Course: OOP Assignment 6
"""

class Employee:
    """
    Represents a general employee.

    Attributes:
        name (str): Employee name
        employee_id (int): Unique ID
    """

    def __init__(self, name: str, employee_id: int):
        self.name = name
        self.employee_id = employee_id

    def get_pay(self) -> float:
        """
        Returns pay amount.
        Must be overridden by subclasses.
        """
        raise NotImplementedError("Subclass must implement get_pay()")

    def get_info(self) -> str:
        """
        Returns basic employee information.
        """
        return f"{self.name} (ID: {self.employee_id})"