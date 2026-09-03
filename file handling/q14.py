'''14.	Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file.'''
with open('student.txt', 'r') as file:
    content = file.read()

old_word = input("Enter the word to be replaced: ")
new_word = input("Enter the new word: ")
content = content.replace(old_word, new_word)

with open('student.txt', 'w') as file:
    file.write(content)

with open('student.txt', 'r') as file:
    modified_content = file.read()
    print("Modified content of the file:")
    print(modified_content)
