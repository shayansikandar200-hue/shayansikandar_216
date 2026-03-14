class Employee:
    """
    Base class representing a generic employee.
    """

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_info(self):
        return f"Employee: {self.name}, ID: {self.employee_id}"

    def get_pay(self):
        raise NotImplementedError("Subclass must implement get_pay()")