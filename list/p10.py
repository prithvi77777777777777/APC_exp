# Q10. Write a program to reverse a list without using the reverse() method.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

numbers = [10, 20, 30, 40, 50]
reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", reversed_list)