import re

filename = input("Enter filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    words = re.findall(r"[A-Za-z]+", text)
    if words:
        longest = max(words, key=len)
        print("Longest word:", longest)
        print("Length:", len(longest))
    else:
        print("No words found.")
except FileNotFoundError:
    print("File not found.")
