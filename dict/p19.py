# Q19. Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

data = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20, "f": 40}

unique_dict = {}
seen_values = []

for key, value in data.items():
    if value not in seen_values:
        unique_dict[key] = value
        seen_values.append(value)

print("Original Dictionary:", data)
print("After Removing Duplicate Values:", unique_dict)