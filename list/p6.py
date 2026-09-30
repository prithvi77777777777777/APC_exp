# Q6. Find the largest and smallest number in a list without using max() or min().
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

numbers = [45, 12, 89, 33, 67, 5, 90, 23]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("List:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)