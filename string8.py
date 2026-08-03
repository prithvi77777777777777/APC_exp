text = input("Enter a string: ")
character = input("Enter a character: ")
count = 0
for item in text:
    if item == character:
        count += 1
print("Frequency:", count)
