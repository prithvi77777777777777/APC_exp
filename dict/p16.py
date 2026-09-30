# Q16. Create two dictionaries and merge them into a single dictionary.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}

merged = {**dict1, **dict2}

print("Dict 1:", dict1)
print("Dict 2:", dict2)
print("Merged Dictionary:", merged)