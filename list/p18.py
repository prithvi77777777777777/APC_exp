# Q18. Create a shopping cart using a list with Add, Remove, Search, Display, Count.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

cart = ["Milk", "Bread", "Eggs"]

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Search Item")
    print("4. Display Cart")
    print("5. Count Total Items")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        cart.append(item)
        print(item, "added to cart.")
    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print(item, "removed from cart.")
        else:
            print(item, "not found in cart.")
    elif choice == 3:
        item = input("Enter item to search: ")
        if item in cart:
            print(item, "is present in cart.")
        else:
            print(item, "is NOT present in cart.")
    elif choice == 4:
        print("Cart Items:", cart)
    elif choice == 5:
        print("Total items in cart:", len(cart))
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")