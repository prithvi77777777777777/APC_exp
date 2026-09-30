# Q24. Store visitor IDs from two different days in separate sets. Determine unique, returning, and single-day visitors.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

day1_visitors = {101, 102, 103, 104, 105}
day2_visitors = {104, 105, 106, 107, 108}

print("Day 1 Visitors:", day1_visitors)
print("Day 2 Visitors:", day2_visitors)
print("Unique visitors across BOTH days:", day1_visitors | day2_visitors)
print("Returning visitors (came both days):", day1_visitors & day2_visitors)
print("Visitors only on DAY 1:", day1_visitors - day2_visitors)
print("Visitors only on DAY 2:", day2_visitors - day1_visitors)