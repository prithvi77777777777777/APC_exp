# Q6. Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

employees = {
    101: "Prithvi",
    102: "Rahul",
    103: "Sneha",
    104: "Amit"
}

emp_id = int(input("Enter employee ID to search: "))

if emp_id in employees:
    print("Employee found:", employees[emp_id])
else:
    print("Employee ID", emp_id, "does NOT exist.")