# Q2. Write a PYTHON program to print the largest of n numbers
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

n = int(input("How many numbers do you want to enter? "))

i = 1
largest = None
while i <= n:
    num = int(input("Enter number " + str(i) + ": "))
    if largest is None or num > largest:
        largest = num
    i += 1

print("Largest number is:", largest)