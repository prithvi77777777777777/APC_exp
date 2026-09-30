# Q34. Take a string, use a dictionary to find the first character that occurs more than once.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

text = input("Enter a string: ")

frequency = {}
result = None

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
        if frequency[ch] == 2 and result is None:
            result = ch
    else:
        frequency[ch] = 1

if result:
    print("First character that occurs more than once:", result)
else:
    print("No character is repeated.")