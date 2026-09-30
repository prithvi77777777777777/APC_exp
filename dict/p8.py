# Q8. Create a dictionary and display all keys, all values, and all key-value pairs.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

data = {
    "name": "Prithvi",
    "roll_no": 115,
    "department": "CSE",
    "marks": 88
}

print("All Keys:", list(data.keys()))
print("All Values:", list(data.values()))
print("All Key-Value Pairs:")
for key, value in data.items():
    print(key, ":", value)