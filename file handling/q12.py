'''12.	Read a text file and count how many times each word occurs. Display the result using a dictionary.'''

with open('student.txt', 'r') as file:
    content = file.read()
    words = content.split()
    word_count = {}
    for i in words:
        if i.isalpha():
            if i in word_count:
                word_count[i] += 1
            else:
                word_count[i] = 1
print("Word count in the file is:", word_count)