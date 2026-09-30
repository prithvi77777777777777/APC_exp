# Q7. Accept 10 numbers from the user and store them in a list. Calculate sum and average.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

numbers = []
for i in range(10):
    n = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(n)

total = sum(numbers)
average = total / len(numbers)

print("List:", numbers)
print("Sum:", total)
print("Average:", average)