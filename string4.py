text = input("Enter a string: ")
cleaned = ""
for character in text.lower():
    if not character.isspace():
        cleaned += character
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
