from collections import Counter
import re

filename = input("Enter filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().lower()

    words = re.findall(r"\\b\\w+\\b", text)
    frequency = dict(Counter(words))
    print("Word frequency:", frequency)
except FileNotFoundError:
    print("File not found.")
