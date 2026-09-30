# Q1. Create a dictionary containing student details such as roll number, name, department, and marks. Display all key-value pairs.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

student = {
    "roll_no": 115,
    "name": "Prithviraj Sutar",
    "department": "CSE",
    "marks": 88
}

print("Student Details:")
for key, value in student.items():
    print(key, ":", value)