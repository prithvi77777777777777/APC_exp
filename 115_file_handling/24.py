# This example uses calculator.py in the same folder.
import calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose +, -, *, /: ")

if operation == "+":
    print(calculator.add(a, b))
elif operation == "-":
    print(calculator.subtract(a, b))
elif operation == "*":
    print(calculator.multiply(a, b))
elif operation == "/":
    print(calculator.divide(a, b))
else:
    print("Invalid operation.")
