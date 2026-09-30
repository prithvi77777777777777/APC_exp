# Q21. Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

squares = {}

for i in range(1, 11):
    squares[i] = i * i

print("Numbers and their Squares:")
for key, value in squares.items():
    print(key, "->", value)