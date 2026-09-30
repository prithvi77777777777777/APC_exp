# Q24. Create a dictionary containing integers from 1 to 10 and their cubes.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

cubes = {}

for i in range(1, 11):
    cubes[i] = i * i * i

print("Numbers and their Cubes:")
for key, value in cubes.items():
    print(key, "->", value)