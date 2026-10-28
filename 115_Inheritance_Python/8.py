class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id, self.name, self.basic_salary = emp_id, name, basic_salary
    def salary(self): return self.basic_salary

class Manager(Employee):
    def salary(self): return self.basic_salary * 1.30

class Developer(Employee):
    def salary(self): return self.basic_salary * 1.20

class Tester(Employee):
    def salary(self): return self.basic_salary * 1.10

for e in [Manager(1, "Maya", 50000), Developer(2, "Raj", 40000), Tester(3, "Om", 35000)]:
    print(e.name, type(e).__name__, "salary: ₹", e.salary())
