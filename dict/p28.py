# Q28. Create a dictionary containing names and phone numbers with Add, Search, Update, Delete, Display.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

contacts = {"Prithvi": "9876543210", "Rahul": "9123456789"}

while True:
    print("\n--- Contact Management Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(name, "added.")
    elif choice == 2:
        name = input("Enter contact name to search: ")
        if name in contacts:
            print(name, "->", contacts[name])
        else:
            print(name, "not found.")
    elif choice == 3:
        name = input("Enter contact name to update: ")
        if name in contacts:
            contacts[name] = input("Enter new phone number: ")
            print("Contact updated.")
        else:
            print(name, "not found.")
    elif choice == 4:
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(name, "deleted.")
        else:
            print(name, "not found.")
    elif choice == 5:
        print("All Contacts:")
        for name, phone in contacts.items():
            print(name, "->", phone)
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")