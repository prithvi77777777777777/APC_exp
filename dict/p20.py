# Q20. Create a dictionary and display its elements in ascending order of keys.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

data = {"banana": 50, "apple": 100, "mango": 80, "cherry": 30}

print("Original Dictionary:", data)
print("Sorted by Keys (Ascending):")
for key in sorted(data.keys()):
    print(key, ":", data[key])