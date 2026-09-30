# Q15. Write a program to determine whether two sets have no elements in common.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

if set1.isdisjoint(set2):
    print("The two sets have NO elements in common.")
else:
    print("The two sets have common elements:", set1 & set2)