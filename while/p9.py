# Q5. Write a PYTHON program find a factorial of given number
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

n = int(input("Enter a number: "))

i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1

print("Factorial of", n, "is:", fact)