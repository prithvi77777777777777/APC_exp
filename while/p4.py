# Q4. Write a PYTHON program to print sum of natural numbers up to n
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

n = int(input("Enter the value of n: "))

i = 1
total = 0
while i <= n:
    total += i
    i += 1

print("Sum of natural numbers up to", n, "is:", total)