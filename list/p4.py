# Q4. Create a list of numbers. Add one at end, one at beginning, one at specified position.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

numbers.append(60)
numbers.insert(0, 5)
numbers.insert(3, 25)

print("Updated list:", numbers)