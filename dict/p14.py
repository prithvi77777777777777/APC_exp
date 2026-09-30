# Q14. Accept a string from the user and create a dictionary containing each character and its frequency.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

text = input("Enter a string: ")

frequency = {}
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character Frequency:")
for key, value in frequency.items():
    print("'"+key+"'", "->", value)