# Examples 15 and 16: multilevel inheritance
class Person:
    def __init__(self, name, age): self.name, self.age = name, age
class Student(Person):
    def __init__(self, name, age, roll, course):
        super().__init__(name, age); self.roll, self.course = roll, course
class ResearchStudent(Student):
    def __init__(self, name, age, roll, course, topic, guide):
        super().__init__(name, age, roll, course); self.topic, self.guide = topic, guide
print(vars(ResearchStudent("Isha", 24, 9, "CSE", "Robotics", "Dr. Rao")))

# Example 17: hierarchical inheritance
class Animal:
    def sound(self): print("Animal sound")
class Dog(Animal):
    def sound(self): print("Woof")
class Cat(Animal):
    def sound(self): print("Meow")
class Cow(Animal):
    def sound(self): print("Moo")
for animal in [Dog(), Cat(), Cow()]: animal.sound()

# Example 18: multiple + hierarchical inheritance
class Doctor(Person):
    pass
class Patient(Person):
    pass
class Surgeon(Doctor):
    def role(self): print(self.name, "is a surgeon")
class MedicalResearcher(Doctor):
    def role(self): print(self.name, "is a medical researcher")
Surgeon("Dr. Mehta", 40).role()
MedicalResearcher("Dr. Khan", 35).role()
