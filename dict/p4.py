# Q4. Create a dictionary containing student marks. Update the marks of a specified student.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

marks = {
    "Prithvi": 88,
    "Rahul": 75,
    "Sneha": 92,
    "Amit": 68
}

print("Original Marks:", marks)

name = input("Enter student name to update marks: ")

if name in marks:
    new_marks = int(input("Enter new marks: "))
    marks[name] = new_marks
    print("Updated Marks:", marks)
else:
    print(name, "not found in dictionary.")