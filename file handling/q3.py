'''3.	Write a program to append additional student information to an existing file without deleting its previous contents.'''
with open('student.txt', 'a') as file:
    address = input("Enter student's address: ")
    file.write(f"Address: {address}\n")

with open('student.txt', 'r') as file:
    content = file.read()
    print("\nUpdated Student Information:")
    print(content)