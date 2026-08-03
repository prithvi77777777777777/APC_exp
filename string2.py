text = input("Enter a string: ")
vowels = consonants = digits = spaces = special = 0
for character in text:
    if character.isalpha():
        if character.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif character.isdigit():
        digits += 1
    elif character.isspace():
        spaces += 1
    else:
        special += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)
