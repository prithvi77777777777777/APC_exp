# Q5. Create a dictionary of cities and their populations. Remove a specified city from the dictionary.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

cities = {
    "Mumbai": 20411000,
    "Pune": 6629000,
    "Delhi": 32941000,
    "Chennai": 10971000,
    "Kolkata": 15134000
}

print("Original Cities:", cities)

city = input("Enter city to remove: ")

if city in cities:
    del cities[city]
    print("Updated Cities:", cities)
else:
    print(city, "not found in dictionary.")