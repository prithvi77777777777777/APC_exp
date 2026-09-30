# Q17. Given two dictionaries, find the keys that are common to both dictionaries.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict2 = {"b": 20, "c": 30, "e": 50, "f": 60}

common_keys = []
for key in dict1:
    if key in dict2:
        common_keys.append(key)

print("Dict 1:", dict1)
print("Dict 2:", dict2)
print("Common Keys:", common_keys)