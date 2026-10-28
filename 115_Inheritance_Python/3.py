class Academic:
    def __init__(self, marks):
        self.marks = marks

class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points

class Student(Academic, Sports):
    def __init__(self, name, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)
        self.name = name

    def overall_performance(self):
        return sum(self.marks) + self.sports_points

s = Student("Riya", [85, 90, 88], 8)
print("Student:", s.name, "| Academic total:", sum(s.marks),
      "| Sports points:", s.sports_points, "| Overall:", s.overall_performance())
