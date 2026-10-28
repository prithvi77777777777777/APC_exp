class PersonalDetails:
    def __init__(self, name, age):
        self.name, self.age = name, age

class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id, self.designation, self.salary = emp_id, designation, salary

class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print(self.name, self.age, self.emp_id, self.designation, f"₹{self.salary}")

Employee("Amit", 28, 501, "Developer", 60000).display()
