# Q2. Write a PYTHON program to print sum of even numbers up to n
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

n = int(input("Enter the value of n: "))

i = 2
total = 0
while i <= n:
    total += i
    i += 2

print("Sum of even numbers up to", n, "is:", total)