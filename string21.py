password = input("Enter a password: ")
has_upper = has_lower = has_digit = has_special = False
for character in password:
    if character.isupper():
        has_upper = True
    elif character.islower():
        has_lower = True
    elif character.isdigit():
        has_digit = True
    else:
        has_special = True
if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Valid password")
else:
    print("Invalid password")
