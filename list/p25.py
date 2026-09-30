# Q25. Remove all duplicate elements while preserving the original order.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

numbers = [10, 20, 10, 30, 20, 40, 50, 30, 60]

unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("After removing duplicates:", unique)