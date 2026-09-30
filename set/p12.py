# Q12. Create two sets of numbers and find the elements present in either set but not in both.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

symmetric_diff = set1 ^ set2
print("Set 1:", set1)
print("Set 2:", set2)
print("Symmetric Difference:", symmetric_diff)