# Q18. Given two dictionaries, identify the values that are common to both dictionaries.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict2 = {"e": 2, "f": 3, "g": 5, "h": 6}

common_values = []
for value in dict1.values():
    if value in dict2.values() and value not in common_values:
        common_values.append(value)

print("Dict 1:", dict1)
print("Dict 2:", dict2)
print("Common Values:", common_values)