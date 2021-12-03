"""
Name: Lesly Endara
sales_force.py

Wasn't able to finish. :(

certification of Authenticity:
I certify that this is entirely my own work
"""
from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        sales_people = []
        self.sales_people = sales_people

    def add_data(self, file_name):
        sales_people = self.sales_people
        file = open(file_name, 'r')
        lines = file.read()
        lines = lines.split("\n")
        for i in range(len(lines)):
            inside = lines[i]
            for ind in inside:
                new_line = inside.split(", ")
                people = SalesPerson(new_line[0], new_line[1])
                ids = people.get_id()
                name = people.get_name()
                sales = new_line[2]
                count = sales.split(" ")
                for ind in range(len(count)):
                    number = eval(count[ind])
                    sales_are = people.enter_sale(number)
                    summ = people.total_sales()
            sales_people.append(ids)
            sales_people.append(name)
            sales_people.append(summ)

    def quota_report(self, quota):
        sales_people = self.sales_people
        report = sales_people
        location = 2
        spot = -1
        for i in range(len(report) // 3):
            totals = sales_people[location]
            print(location)
            print(report[location])
            spot += 4
            if totals == quota:
                answer = True
            else:
                answer = False
            print(answer)
            report.insert(spot, answer)
        print(report)
        return report

    def top_seller(self):  # -> list[SalesPerson] - returns a list of SalesPerson objects with the highest sales amount.
        # If there are no ties, the list should contain one record. In the case of a tie, the list should include all
        # of the top sales people.
        sales_people = self.sales_people
        for i in range(len(sales_people)):
            return

    def individual_sales(self, employee_id):  # -> SalesPerson - returns the SalesPerson with the given employee_id or
        # None if the id does not exist.
        sales_people = self.sales_people