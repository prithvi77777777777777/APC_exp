# Q2. Create a dictionary containing employee information and display the value associated with a specified key.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

employee = {
    "emp_id": 101,
    "name": "Prithvi",
    "department": "IT",
    "salary": 55000
}

key = input("Enter the key to display value: ")

if key in employee:
    print(key, ":", employee[key])
else:
    print("Key not found in dictionary.")