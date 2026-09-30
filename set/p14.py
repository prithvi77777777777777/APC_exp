# Q14. Create two sets and determine whether the first set is a superset of the second set.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3}

print("Set 1:", set1)
print("Set 2:", set2)

if set1.issuperset(set2):
    print("Set 1 is a SUPERSET of Set 2")
else:
    print("Set 1 is NOT a superset of Set 2")