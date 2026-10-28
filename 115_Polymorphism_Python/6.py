class Student:
    def __init__(self, marks): self.marks = marks
    def calculate_grade(self): return "Not specified"
class EngineeringStudent(Student):
    def calculate_grade(self): return "Pass" if self.marks >= 40 else "Fail"
class MedicalStudent(Student):
    def calculate_grade(self): return "Distinction" if self.marks >= 75 else "Pass" if self.marks >= 50 else "Fail"
class ManagementStudent(Student):
    def calculate_grade(self): return "A" if self.marks >= 80 else "B" if self.marks >= 60 else "C"
for s in [EngineeringStudent(67), MedicalStudent(82), ManagementStudent(74)]:
    print(type(s).__name__, s.calculate_grade())
