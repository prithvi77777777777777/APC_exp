# Q17. Create two 3x3 matrices using nested lists and perform matrix addition.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("Matrix 1:")
for row in matrix1:
    print(row)

print("Matrix 2:")
for row in matrix2:
    print(row)

print("Result (Matrix Addition):")
for row in result:
    print(row)