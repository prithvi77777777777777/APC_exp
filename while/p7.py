# Q3. Write a PYTHON program to print natural numbers up to n in reverse order.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

n = int(input("Enter the value of n: "))

i = n
while i >= 1:
    print(i, end=" ")
    i -= 1
print()