# Q4. Create a set of numbers and remove a specified number from the set.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

numbers = {10, 20, 30, 40, 50}
print("Original Set:", numbers)

num = int(input("Enter number to remove: "))
if num in numbers:
    numbers.remove(num)
    print("Updated Set:", numbers)
else:
    print(num, "not found in set.")