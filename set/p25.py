# Q25. Represent the friends of two users using sets. Find mutual friends, friends unique to each user, and total unique friends.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

user1_friends = {"Rahul", "Sneha", "Amit", "Priya", "Rohit"}
user2_friends = {"Sneha", "Priya", "Karan", "Nisha", "Rohit"}

print("User 1 Friends:", user1_friends)
print("User 2 Friends:", user2_friends)
print("Mutual Friends:", user1_friends & user2_friends)
print("Friends unique to User 1:", user1_friends - user2_friends)
print("Friends unique to User 2:", user2_friends - user1_friends)
print("Total Unique Friends:", user1_friends | user2_friends)