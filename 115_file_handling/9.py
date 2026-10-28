import string

filename = input("Enter filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().lower()

    vowels = sum(1 for ch in text if ch in "aeiou")
    consonants = sum(1 for ch in text if ch in string.ascii_lowercase and ch not in "aeiou")
    print("Vowels:", vowels)
    print("Consonants:", consonants)
except FileNotFoundError:
    print("File not found.")
