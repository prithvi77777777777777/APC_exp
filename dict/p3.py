# Q3. Create a dictionary of five products and their prices. Add a new product and price to the dictionary.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

products = {
    "Laptop": 55000,
    "Mobile": 25000,
    "Tablet": 18000,
    "Headphones": 2000,
    "Keyboard": 1500
}

print("Original Products:")
for key, value in products.items():
    print(key, ":", value)

name = input("\nEnter new product name: ")
price = float(input("Enter product price: "))
products[name] = price

print("\nUpdated Products:")
for key, value in products.items():
    print(key, ":", value)