# Q10. Accept five student names and their marks from the user and store them in a dictionary.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

students = {}

for i in range(5):
    name = input("Enter student name " + str(i + 1) + ": ")
    marks = int(input("Enter marks of " + name + ": "))
    students[name] = marks

print("\nStudent Dictionary:", students)