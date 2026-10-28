from student.marks import total, percentage
from student.grade import grade
from student.attendance import eligible

marks = [80, 85, 90, 75, 88]
print("Total:", total(marks))
print("Percentage:", percentage(marks))
print("Grade:", grade(percentage(marks)))
print("Attendance eligible:", eligible(80))
