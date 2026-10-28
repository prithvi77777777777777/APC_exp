class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id, self.name, self.salary = emp_id, name, salary

    def display(self):
        print(f"ID: {self.emp_id}\nName: {self.name}\nSalary: ₹{self.salary:.2f}")

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)
        print(f"Annual salary: ₹{self.salary * 12:.2f}")

Manager(101, "Asha", 50000, "IT").display()
