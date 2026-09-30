# Q30. Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

students = {
    "Prithvi": "CSE",
    "Rahul": "IT",
    "Sneha": "CSE",
    "Amit": "ENTC",
    "Priya": "IT",
    "Rohit": "CSE"
}

grouped = {}

for name, dept in students.items():
    if dept in grouped:
        grouped[dept].append(name)
    else:
        grouped[dept] = [name]

print("Original Dictionary:", students)
print("\nGrouped by Department:")
for dept, names in grouped.items():
    print(dept, "->", names)