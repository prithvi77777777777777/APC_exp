'''13.	Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.'''
str=input("Enter a word to search: ")
with open('student.txt', 'r') as file:
    content = file.read()
    words=content.split()
    if str in words:
        count=words.count(str)
        print(f"The word '{str}' occurs {count} times in the file.")