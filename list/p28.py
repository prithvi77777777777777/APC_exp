# Q28. Store scores of a batsman in 10 matches and calculate statistics.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

scores = []
for i in range(10):
    s = int(input("Enter score of match " + str(i + 1) + ": "))
    scores.append(s)

highest = scores[0]
lowest = scores[0]
total = 0

for s in scores:
    if s > highest:
        highest = s
    if s < lowest:
        lowest = s
    total += s

average = total / len(scores)

centuries = 0
half_centuries = 0
for s in scores:
    if s >= 100:
        centuries += 1
    elif 50 <= s <= 99:
        half_centuries += 1

print("Scores:", scores)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Number of centuries:", centuries)
print("Number of half-centuries:", half_centuries)