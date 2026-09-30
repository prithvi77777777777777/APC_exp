# Q23. Count the frequency of each element in a list.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

numbers = [10, 20, 10, 30, 20, 10, 40, 50, 30]

frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("List:", numbers)
print("Frequency of each element:")
for key, value in frequency.items():
    print(key, "->", value, "times")