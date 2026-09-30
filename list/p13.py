# Q13. Accept 10 numbers and sort them in ascending and descending order.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

numbers = []
for i in range(10):
    n = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(n)

print("Original list:", numbers)

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending order:", ascending)
print("Descending order:", descending)