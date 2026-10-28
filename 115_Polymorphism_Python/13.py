class Person:
    def display_role(self): print("Person")
class Student(Person):
    def display_role(self): print("Student")
class Faculty(Person):
    def display_role(self): print("Faculty")
class Administrator(Person):
    def display_role(self): print("Administrator")
for person in [Student(), Faculty(), Administrator()]: person.display_role()
