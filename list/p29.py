# Q29. Store temperature of 30 days and determine hottest, coldest, average, above/below average.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

temps = []
for i in range(30):
    t = float(input("Enter temperature of day " + str(i + 1) + ": "))
    temps.append(t)

hottest = temps[0]
coldest = temps[0]
total = 0

for t in temps:
    if t > hottest:
        hottest = t
    if t < coldest:
        coldest = t
    total += t

average = total / len(temps)

above_avg = 0
below_avg = 0
for t in temps:
    if t > average:
        above_avg += 1
    elif t < average:
        below_avg += 1

print("Temperatures:", temps)
print("Hottest day temperature:", hottest)
print("Coldest day temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above_avg)
print("Days below average:", below_avg)