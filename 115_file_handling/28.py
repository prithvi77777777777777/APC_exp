import salary_utils

basic = float(input("Enter basic salary: ₹"))
gross = salary_utils.gross_salary(basic)
deductions = salary_utils.deductions(basic)
print("Gross salary: ₹", gross)
print("Deductions: ₹", deductions)
print("Net salary: ₹", gross - deductions)
