# Q2. Write a PYTHON program to find the sum of digits of given number
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

n = int(input("Enter a number: "))

temp = n
total = 0
while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

print("Sum of digits of", n, "is:", total)