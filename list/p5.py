# Q5. Create a list of student names. Remove first, last, and a specific student by name.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

students = ["Prithvi", "Rahul", "Amit", "Sneha", "Priya"]
print("Original list:", students)

students.pop(0)
students.pop(-1)

name = input("Enter student name to remove: ")
if name in students:
    students.remove(name)

print("Remaining list:", students)