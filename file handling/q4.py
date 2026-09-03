'''4.	Write a program to read a text file line by line and display each line separately.'''
with open('student.txt', 'r') as file:
    text = file.readlines()
    print("Contents of the File (Line by Line):")
    for line in text:
        print(line.strip())

