# Q27. Store salaries of employees and determine highest, lowest, average, above 50k, below 30k.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

n = int(input("Enter number of employees: "))
salaries = []
for i in range(n):
    s = float(input("Enter salary of employee " + str(i + 1) + ": "))
    salaries.append(s)

highest = salaries[0]
lowest = salaries[0]
total = 0

for s in salaries:
    if s > highest:
        highest = s
    if s < lowest:
        lowest = s
    total += s

average = total / len(salaries)

above_50k = 0
below_30k = 0
for s in salaries:
    if s > 50000:
        above_50k += 1
    if s < 30000:
        below_30k += 1

print("Salaries:", salaries)
print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Employees earning above Rs.50,000:", above_50k)
print("Employees earning below Rs.30,000:", below_30k)