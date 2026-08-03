text = input("Enter a string: ")
if text:
    most_frequent = text[0]
    for character in text:
        if text.count(character) > text.count(most_frequent):
            most_frequent = character
    print("Most frequent character:", most_frequent)
else:
    print("The string is empty.")
