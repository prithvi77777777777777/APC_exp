# Q4. Write a PYTHON program to print Fibonacci series up to n
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

n = int(input("Enter the number of terms: "))

a = 0
b = 1
i = 1
while i <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    i += 1
print()