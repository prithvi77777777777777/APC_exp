# Q22. Find common elements between two lists.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []
for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", common)