text = input("Enter a string: ")
printed = set()
for character in text:
    if text.count(character) > 1 and character not in printed:
        print(character)
        printed.add(character)
