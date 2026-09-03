'''2.	Write a program to open a text file and display its complete contents.'''
with open('student.txt', 'r') as file:
    content = file.read()
    print("Complete Contents of the File:")
    print(content)