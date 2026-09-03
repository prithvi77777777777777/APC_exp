'''1.	Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file.'''         
with open('student.txt', 'w') as file:
    name = input("Enter student's name: ")
    roll_number = input("Enter roll number: ")
    branch = input("Enter branch: ")
    semester = input("Enter semester: ")

    file.write(f"Name: {name}\n")
    file.write(f"Roll Number: {roll_number}\n")
    file.write(f"Branch: {branch}\n")
    file.write(f"Semester: {semester}\n")
with open('student.txt', 'r') as file:
    content = file.read()
    print("\nStudent Information:")
    print(content)