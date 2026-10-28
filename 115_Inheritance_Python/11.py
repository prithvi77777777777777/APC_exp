class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no, self.name, self.course = roll_no, name, course

class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course); self.marks = marks

    def display_result(self):
        total = sum(self.marks); percentage = total / len(self.marks)
        grade = "A" if percentage >= 80 else "B" if percentage >= 60 else "C" if percentage >= 40 else "F"
        print(self.roll_no, self.name, self.course, "| Total:", total,
              "| Percentage:", percentage, "% | Grade:", grade)

Result(7, "Sana", "CSE", [88, 76, 91]).display_result()
