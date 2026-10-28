class Employee:
    def __init__(self, name, basic): self.name, self.basic = name, basic
    def calculate_salary(self): return self.basic
class Manager(Employee):
    def calculate_salary(self): return self.basic + 15000
class Developer(Employee):
    def calculate_salary(self): return self.basic + 10000
class Tester(Employee):
    def calculate_salary(self): return self.basic + 7000
for e in [Manager("Asha", 50000), Developer("Ravi", 40000), Tester("Mina", 35000)]:
    print(e.name, e.calculate_salary())
