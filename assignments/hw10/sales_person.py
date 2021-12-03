"""
Name: Lesly Endara
sales_person.py


certification of Authenticity:
I certify that this is entirely my own work
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):  # -> returns the sales person’s employee_id
        employee_id = self.employee_id
        return int(employee_id)

    def get_name(self):  # -> returns the sales person’s name
        name = self.name
        return str(name)

    def set_name(self, name):  # sets the sales person’s name
        name = self.name

    def enter_sale(self, sale):  # adds the value of sale to the sales list
        sale_list = self.sales
        sale_list.append(sale)

    def total_sales(self):  # returns the sum of the sales person’s sales
        sales_list = self.sales
        total_sales = sum(sales_list)
        return float(total_sales)

    def get_sales(self):  # -> returns the list of sales
        sales_list = self.sales
        return list(sales_list)

    def met_quota(self, quota):  # returns True if the total sales meet or exceed the quota provided, or returns False
        total = self.total_sales()
        if total >= quota:
            return True
        else:
            return False

    def compare_to(self, other):  # other is another SalesPerson.returns - 1 if other has more in total sales
        # than self, 1 if self has more in total sales than other, and 0 if their total sales are the same
        total_sales = self.total_sales()
        if total_sales < other:
            return -1
        elif total_sales == other:
            return 0
        else:
            return 1

    def __str__(self):  # -> string - returns “ < employee_id > - < name >: < total sales >"
        return '['+self.employee_id+' '+self.name+' '+str(self.total_sales())+']'
