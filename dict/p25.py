# Q25. Create a dictionary containing student names and marks with Add, Update, Delete, Search, Display, Highest, Average.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

students = {"Prithvi": 88, "Rahul": 75, "Sneha": 92}

while True:
    print("\n--- Student Management Menu ---")
    print("1. Add a Student")
    print("2. Update Marks")
    print("3. Delete a Student")
    print("4. Search for a Student")
    print("5. Display All Students")
    print("6. Find Highest Marks")
    print("7. Calculate Average")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print(name, "added.")
    elif choice == 2:
        name = input("Enter student name to update: ")
        if name in students:
            students[name] = int(input("Enter new marks: "))
            print("Marks updated.")
        else:
            print(name, "not found.")
    elif choice == 3:
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print(name, "deleted.")
        else:
            print(name, "not found.")
    elif choice == 4:
        name = input("Enter student name to search: ")
        if name in students:
            print(name, "-> Marks:", students[name])
        else:
            print(name, "not found.")
    elif choice == 5:
        print("All Students:")
        for name, marks in students.items():
            print(name, "->", marks)
    elif choice == 6:
        if students:
            highest = max(students, key=students.get)
            print("Highest Marks:", highest, "->", students[highest])
        else:
            print("No students.")
    elif choice == 7:
        if students:
            total = sum(students.values())
            print("Average Marks:", total / len(students))
        else:
            print("No students.")
    elif choice == 8:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")