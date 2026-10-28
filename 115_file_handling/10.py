import string

filename = input("Enter filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    alphabets = sum(ch.isalpha() for ch in text)
    digits = sum(ch.isdigit() for ch in text)
    spaces = sum(ch == " " for ch in text)
    special = sum(not ch.isalnum() and not ch.isspace() for ch in text)

    print("Alphabets:", alphabets)
    print("Digits:", digits)
    print("Spaces:", spaces)
    print("Special characters:", special)
except FileNotFoundError:
    print("File not found.")
