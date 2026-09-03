'''10.	Read a text file and calculate the number of alphabets, digits, spaces, and special characters.'''

with open('student.txt', 'r') as file:
    content= file.read()
    alphabets=0
    spaces=0
    digits=0
    special_characters=0
    for i in content:
        if i.isalpha():
            alphabets+=1
        elif i.isspace():
            spaces+=1
        elif i.isdigit():
            digits+=1
        else:
            special_characters+=1

print(f"Number of alphabets: {alphabets}")
print(f"Number of spaces: {spaces}")
print(f"Number of digits: {digits}")
print(f"Number of special characters: {special_characters}")