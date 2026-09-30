# Q8. Create a list containing duplicate numbers, use a set to remove the duplicates.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

numbers = [10, 20, 10, 30, 20, 40, 50, 30, 60, 10]
print("Original List:", numbers)

unique_numbers = list(set(numbers))
print("After Removing Duplicates:", unique_numbers)