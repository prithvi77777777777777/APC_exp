# Q29. Create a dictionary containing book IDs and book names with Add, Search, Remove, Display, Count.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

books = {101: "Python Basics", 102: "Data Structures", 103: "Operating Systems"}

while True:
    print("\n--- Book Management Menu ---")
    print("1. Add a Book")
    print("2. Search a Book")
    print("3. Remove a Book")
    print("4. Display All Books")
    print("5. Count Total Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        name = input("Enter book name: ")
        books[book_id] = name
        print(name, "added.")
    elif choice == 2:
        book_id = int(input("Enter book ID to search: "))
        if book_id in books:
            print("Book Found:", books[book_id])
        else:
            print("Book ID", book_id, "not found.")
    elif choice == 3:
        book_id = int(input("Enter book ID to remove: "))
        if book_id in books:
            del books[book_id]
            print("Book removed.")
        else:
            print("Book ID", book_id, "not found.")
    elif choice == 4:
        print("All Books:")
        for book_id, name in books.items():
            print(book_id, "->", name)
    elif choice == 5:
        print("Total books:", len(books))
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")