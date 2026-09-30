# Q9. Create a list of cities. Ask user to enter a city and check if it exists.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

cities = ["Mumbai", "Pune", "Delhi", "Chennai", "Kolkata", "Bangalore"]

city = input("Enter a city name: ")
if city in cities:
    print(city, "exists in the list.")
else:
    print(city, "does NOT exist in the list.")