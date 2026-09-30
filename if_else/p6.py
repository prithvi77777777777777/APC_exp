# Q2. Write a PYTHON program to find largest of three numbers.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)