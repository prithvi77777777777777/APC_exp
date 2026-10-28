class Student:
    def __init__(self, name, marks): self.name, self.marks = name, marks
    def __gt__(self, other): return self.marks > other.marks
    def __lt__(self, other): return self.marks < other.marks
a, b = Student("Asha", 89), Student("Riya", 82)
print(a.name, ">", b.name, ":", a > b)
print(a.name, "<", b.name, ":", a < b)
