'''11.	Read a text file and find the longest word present in the file.'''

with open('student.txt', 'r') as file:
    content = file.read()
    words = content.split()
    longest_word = 0
    for i in words:
        if len(i) > longest_word:
            longest_word = len(i)
            word = i
    print(f"The longest word in the file is: {word}")