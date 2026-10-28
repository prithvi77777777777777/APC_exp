import csv

def read_employees(filename="employees.csv"):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    for row in rows:
        row["Salary"] = float(row["Salary"])
    return rows

def display_employees(employees):
    for employee in employees:
        print(employee)

def highest_paid_employee(employees):
    return max(employees, key=lambda employee: employee["Salary"])

def average_salary(employees):
    return sum(employee["Salary"] for employee in employees) / len(employees) if employees else 0

def above_salary(employees, limit):
    return [employee for employee in employees if employee["Salary"] > limit]

try:
    employees = read_employees()
    display_employees(employees)
    if employees:
        print("Highest-paid employee:", highest_paid_employee(employees))
        print("Average salary:", average_salary(employees))
        limit = float(input("Display employees earning above ₹: "))
        print(above_salary(employees, limit))
except FileNotFoundError:
    print("employees.csv not found.")
