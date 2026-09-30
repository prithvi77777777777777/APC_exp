# Q26. Create a dictionary containing employee names and salaries. Find highest, lowest, average, and employees earning more than Rs.50,000.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

employees = {
    "Prithvi": 65000,
    "Rahul": 45000,
    "Sneha": 72000,
    "Amit": 28000,
    "Priya": 55000
}

highest_name = max(employees, key=employees.get)
lowest_name = min(employees, key=employees.get)
total = sum(employees.values())
average = total / len(employees)

print("Employee Salaries:", employees)
print("Highest Salary:", highest_name, "->", employees[highest_name])
print("Lowest Salary:", lowest_name, "->", employees[lowest_name])
print("Average Salary:", average)

print("Employees earning more than Rs.50,000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, "->", salary)