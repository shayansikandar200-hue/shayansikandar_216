from hourly_employee import HourlyEmployee
from commission_employee import CommissionEmployee


employees = [
    HourlyEmployee("Alice", 1, 20),
    CommissionEmployee("Bob", 2, 0.10)
]

employees[0].add_hours(10)
employees[1].add_sale(1000)

for emp in employees:
    print(emp.get_info())
    print("Pay:", emp.get_pay())