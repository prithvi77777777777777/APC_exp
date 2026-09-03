'''7.	Write a program to count the total number of characters in a text file, including spaces.'''
with open('student.txt', 'r') as file:
    content = file.read()
    total_characters = len(content)
    print(f"Total number of characters in the file (including spaces): {total_characters}")
    print("Characters in the file are:", content)