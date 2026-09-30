# Q22. Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i * i

print("Even Numbers and their Squares:")
for key, value in squares.items():
    print(key, "->", value)