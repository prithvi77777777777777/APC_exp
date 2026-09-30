# Q32. Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

numbers = [2, 7, 11, 15, 3, 6]
target = 9

seen = {}
found = False

for num in numbers:
    complement = target - num
    if complement in seen:
        print("Pair found:", complement, "and", num, "=", target)
        found = True
        break
    seen[num] = True

if not found:
    print("No pair found with sum", target)