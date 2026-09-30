# Q12. Create a dictionary containing student names and marks. Find the student with the lowest marks.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

students = {
    "Prithvi": 88,
    "Rahul": 75,
    "Sneha": 92,
    "Amit": 68,
    "Priya": 85
}

lowest_name = None
lowest_marks = 999999

for name, marks in students.items():
    if marks < lowest_marks:
        lowest_marks = marks
        lowest_name = name

print("Student with lowest marks:", lowest_name, "->", lowest_marks)