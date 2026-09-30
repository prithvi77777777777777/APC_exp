# Q15. Find the second largest element in a list.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

numbers = [45, 12, 89, 33, 67, 5, 90, 23]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("List:", numbers)
print("Second largest element:", second_largest)