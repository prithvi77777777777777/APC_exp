class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no, self.course = roll_no, course

class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic, self.guide = topic, guide

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nRoll No: {self.roll_no}"
              f"\nCourse: {self.course}\nResearch: {self.topic}\nGuide: {self.guide}")

ResearchStudent("Neha", 23, 12, "CSE", "AI in Healthcare", "Dr. Patil").display()
