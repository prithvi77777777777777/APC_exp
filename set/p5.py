# Q5. Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

students = {"Prithvi", "Rahul", "Sneha", "Amit", "Priya"}

name = input("Enter student name to search: ")
if name in students:
    print(name, "exists in the set.")
else:
    print(name, "does NOT exist in the set.")