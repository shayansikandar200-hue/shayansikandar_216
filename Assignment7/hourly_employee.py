from employee import Employee


class HourlyEmployee(Employee):

    def __init__(self, name, employee_id, hourly_rate):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def add_hours(self, hours):
        self.hours_worked += hours

    def get_pay(self):
        return self.hourly_rate * self.hours_worked