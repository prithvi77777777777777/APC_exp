# Q3. Write a PYTHON program to print smallest of n numbers
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

n = int(input("How many numbers do you want to enter? "))

i = 1
smallest = None
while i <= n:
    num = int(input("Enter number " + str(i) + ": "))
    if smallest is None or num < smallest:
        smallest = num
    i += 1

print("Smallest number is:", smallest)