

user1_friends = {"Aman", "Bhavna", "Chetan", "Divya"}
user2_friends = {"Chetan", "Divya", "Esha", "Farhan"}

print("Mutual friends:", user1_friends.intersection(user2_friends))
print("Friends unique to User 1:", user1_friends.difference(user2_friends))
print("Friends unique to User 2:", user2_friends.difference(user1_friends))
print("Total unique friends:", user1_friends.union(user2_friends))
