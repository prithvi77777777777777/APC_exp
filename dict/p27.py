# Q27. Create a dictionary containing product names and quantities with Add, Update, Delete, Search, Display products with quantity below 10.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

products = {"Laptop": 5, "Mobile": 15, "Tablet": 8, "Keyboard": 20}

while True:
    print("\n--- Product Management Menu ---")
    print("1. Add a Product")
    print("2. Update Quantity")
    print("3. Delete a Product")
    print("4. Search for a Product")
    print("5. Display Products with Quantity below 10")
    print("6. Display All Products")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        products[name] = qty
        print(name, "added.")
    elif choice == 2:
        name = input("Enter product name to update: ")
        if name in products:
            products[name] = int(input("Enter new quantity: "))
            print("Quantity updated.")
        else:
            print(name, "not found.")
    elif choice == 3:
        name = input("Enter product name to delete: ")
        if name in products:
            del products[name]
            print(name, "deleted.")
        else:
            print(name, "not found.")
    elif choice == 4:
        name = input("Enter product name to search: ")
        if name in products:
            print(name, "-> Quantity:", products[name])
        else:
            print(name, "not found.")
    elif choice == 5:
        print("Products with Quantity below 10:")
        for name, qty in products.items():
            if qty < 10:
                print(name, "->", qty)
    elif choice == 6:
        print("All Products:", products)
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")