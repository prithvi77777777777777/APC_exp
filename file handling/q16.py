'''16.	Read a text file and create another file containing the same text in uppercase.'''
with open('student.txt','r') as file:
    content=file.readlines()
with open('uppercase.txt', 'w') as nfile:
    for i in content:
        nfile.write(i.upper())