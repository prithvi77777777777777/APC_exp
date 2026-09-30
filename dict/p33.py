# Q33. Take a string, use a dictionary to find the first character that occurs only once.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

text = input("Enter a string: ")

frequency = {}
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

result = None
for ch in text:
    if frequency[ch] == 1:
        result = ch
        break

if result:
    print("First character that occurs only once:", result)
else:
    print("No character occurs only once.")