'''6.	Write a program to count the total number of words present in a text file.'''
with open('student.txt', 'r') as file:
    content =file.read()
    words=content.split()
    print(f"Total number of words in the file: {len(words)}")
    print("Words in the file are:", words)