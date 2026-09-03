'''8.	Write a program to read a text file and display its lines in reverse order.'''
with open('student.txt', 'r') as file:
    lines = file.readlines()
    reversed_lines = lines[::-1]
    print("Lines in reverse order:")
    for line in reversed_lines:
        print(line.strip())