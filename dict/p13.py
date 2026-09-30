# Q13. Create a dictionary containing student names and marks. Calculate the average marks of all students.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

students = {
    "Prithvi": 88,
    "Rahul": 75,
    "Sneha": 92,
    "Amit": 68,
    "Priya": 85
}

total = 0
for marks in students.values():
    total += marks

average = total / len(students)
print("Total marks:", total)
print("Average marks:", average)