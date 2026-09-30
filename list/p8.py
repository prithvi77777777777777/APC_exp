# Q8. Store 15 integers in a list. Count how many are even and odd.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

numbers = []
for i in range(15):
    n = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(n)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("List:", numbers)
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)