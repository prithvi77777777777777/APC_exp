text = input("Enter a string: ")
uppercase = lowercase = 0
for character in text:
    if character.isupper():
        uppercase += 1
    elif character.islower():
        lowercase += 1
print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
