# Q11. Create two sets and find elements present in first but not second, and second but not first.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

only_in_first = set1 - set2
only_in_second = set2 - set1

print("Set 1:", set1)
print("Set 2:", set2)
print("Elements in Set 1 but not in Set 2:", only_in_first)
print("Elements in Set 2 but not in Set 1:", only_in_second)