# Q20. Create a list of books. Add, Search, Remove, Display, Count.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

books = ["Python Basics", "Data Structures", "Operating Systems", "DBMS"]

while True:
    print("\n--- Library Menu ---")
    print("1. Add a New Book")
    print("2. Search a Book")
    print("3. Remove a Book")
    print("4. Display All Books")
    print("5. Count Total Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name to add: ")
        books.append(book)
        print(book, "added.")
    elif choice == 2:
        book = input("Enter book name to search: ")
        if book in books:
            print(book, "is available.")
        else:
            print(book, "is NOT available.")
    elif choice == 3:
        book = input("Enter book name to remove: ")
        if book in books:
            books.remove(book)
            print(book, "removed.")
        else:
            print(book, "not found.")
    elif choice == 4:
        print("Books in Library:", books)
    elif choice == 5:
        print("Total books:", len(books))
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")