# Q13. Create two sets and determine whether the first set is a subset of the second set.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)

if set1.issubset(set2):
    print("Set 1 is a SUBSET of Set 2")
else:
    print("Set 1 is NOT a subset of Set 2")