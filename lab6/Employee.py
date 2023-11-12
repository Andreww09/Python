# ex4

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, experience):
        super().__init__(name, 10000)
        self.experience = experience

    def employee_info(self, employee):
        if isinstance(employee, Engineer):
            print(f"{employee.get_name()} is an Engineer with a salary of {employee.get_salary()}")
        elif isinstance(employee, SalesPerson):
            print(f"{employee.get_name()} is a Sales Person with a salary of {employee.get_salary()}")
        else:
            print(f"No info available")


class Engineer(Employee):
    def __init__(self, name, projects_completed):
        super().__init__(name, 8000)
        self.projects_completed = projects_completed

    def work(self):
        print(f"{self.name} started work on project {self.projects_completed + 1}")


class SalesPerson(Employee):
    def __init__(self, name):
        super().__init__(name, 4500)
        self.sales = []

    def add_sale_transaction(self, day, amount):
        self.sales.append((day, amount))

    def create_sales_report(self):
        print(f"{self.name}'s sales report:")
        for day, amount in self.sales:
            print(f"Day {day} : {amount}")
        print()


manager = Manager("Person1", 10)
engineer = Engineer("Person2", 20)
salesperson = SalesPerson("Person3")

engineer.work()

salesperson.add_sale_transaction(1, 100)
salesperson.add_sale_transaction(2, 101)
salesperson.create_sales_report()

manager.employee_info(salesperson)
manager.employee_info(engineer)
manager.employee_info(manager)
