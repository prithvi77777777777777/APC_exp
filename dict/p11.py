# Q11. Create a dictionary containing student names and marks. Find the student who has scored the highest marks.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

students = {
    "Prithvi": 88,
    "Rahul": 75,
    "Sneha": 92,
    "Amit": 68,
    "Priya": 85
}

highest_name = None
highest_marks = -1

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_name = name

print("Student with highest marks:", highest_name, "->", highest_marks)