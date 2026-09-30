# Q16. Create a nested list storing Student Name, Roll Number, Marks. Display all details.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

students = [
    ["Prithvi", 115, 88],
    ["Rahul", 116, 75],
    ["Sneha", 117, 92],
    ["Amit", 118, 68]
]

print("Student Details:")
print("-" * 35)
for student in students:
    print("Name:", student[0], "| Roll No:", student[1], "| Marks:", student[2])