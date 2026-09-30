# Q26. Store marks of 20 students and determine highest, lowest, average, above/below average.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

marks = []
for i in range(20):
    m = int(input("Enter marks of student " + str(i + 1) + ": "))
    marks.append(m)

highest = marks[0]
lowest = marks[0]
total = 0

for m in marks:
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m
    total += m

average = total / len(marks)

above_avg = 0
below_avg = 0
for m in marks:
    if m > average:
        above_avg += 1
    elif m < average:
        below_avg += 1

print("Marks:", marks)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", above_avg)
print("Students below average:", below_avg)