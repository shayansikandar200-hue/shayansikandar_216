from employee import Employee


class CommissionEmployee(Employee):

    def __init__(self, name, employee_id, commission_rate):
        super().__init__(name, employee_id)
        self.commission_rate = commission_rate
        self.sales = 0

    def add_sale(self, amount):
        self.sales += amount

    def get_pay(self):
        return self.sales * self.commission_rate