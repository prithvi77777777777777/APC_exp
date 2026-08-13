# Visitor IDs recorded on two days
day1_visitors = {101, 102, 103, 104, 105}
day2_visitors = {103, 104, 105, 106, 107}

print("Unique visitors across both days:", day1_visitors.union(day2_visitors))
print("Returning visitors:", day1_visitors.intersection(day2_visitors))
print("Visitors only on the first day:", day1_visitors.difference(day2_visitors))
print("Visitors only on the second day:", day2_visitors.difference(day1_visitors))

# Products that may be in more than one category
electronics = {"Laptop", "Smartphone", "Headphones", "Smartwatch"}
accessories = {"Headphones", "Smartwatch", "Charger", "Phone Case"}

print("Products in both categories:", electronics.intersection(accessories))
