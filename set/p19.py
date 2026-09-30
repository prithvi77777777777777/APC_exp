# Q19. Create two sets: students present in morning and afternoon sessions. Find various results.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

morning = {"Prithvi", "Rahul", "Sneha", "Amit"}
afternoon = {"Sneha", "Amit", "Priya", "Rohit"}

print("Morning Session:", morning)
print("Afternoon Session:", afternoon)
print("Students present in BOTH sessions:", morning & afternoon)
print("Students present only in MORNING:", morning - afternoon)
print("Students present only in AFTERNOON:", afternoon - morning)
print("Students present in AT LEAST ONE session:", morning | afternoon)