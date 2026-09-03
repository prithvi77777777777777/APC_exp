'''15.	Read a Python source file and create another file after removing single-line comments.'''
with open('student.txt', 'r') as file:
    content= file.readlines()
with open('new_student.txt', 'w') as new_file:
    for i in content:
        if not i.strip().startswith('#'):
            new_file.write(i)
with open('new_student.txt', 'r') as new_file:
    modified_content = new_file.read()
    print("Content of the new file after removing single-line comments:")
    print(modified_content)