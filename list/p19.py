# Q19. Store names of students present in class. Display total, search, add, remove.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

present_students = ["Prithvi", "Rahul", "Sneha", "Amit"]

while True:
    print("\n--- Class Attendance Menu ---")
    print("1. Display Total Students")
    print("2. Search a Student")
    print("3. Add a New Student")
    print("4. Remove an Absent Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Total students present:", len(present_students))
    elif choice == 2:
        name = input("Enter student name to search: ")
        if name in present_students:
            print(name, "is PRESENT.")
        else:
            print(name, "is ABSENT.")
    elif choice == 3:
        name = input("Enter new student name: ")
        present_students.append(name)
        print(name, "added.")
    elif choice == 4:
        name = input("Enter absent student name to remove: ")
        if name in present_students:
            present_students.remove(name)
            print(name, "removed.")
        else:
            print(name, "not found.")
    elif choice == 5:
        print("Students Present:", present_students)
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")