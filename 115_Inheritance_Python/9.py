class Person:
    def __init__(self, name): self.name = name

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name); self.course = course

class Faculty(Person):
    def __init__(self, name, subject):
        super().__init__(name); self.subject = subject

class TeachingAssistant(Student, Faculty):
    def __init__(self, name, course, subject):
        Student.__init__(self, name, course)
        Faculty.__init__(self, name, subject)

    def display(self):
        print(self.name, "| Course:", self.course, "| Subject:", self.subject)

TeachingAssistant("Kiran", "CSE", "Python").display()
