import re

filename = input("Enter filename: ")
target = input("Enter word to search: ").lower()
total = 0
line_numbers = []

try:
    with open(filename, "r", encoding="utf-8") as file:
        for line_no, line in enumerate(file, start=1):
            count = len(re.findall(r"\\b" + re.escape(target) + r"\\b", line, re.IGNORECASE))
            if count:
                total += count
                line_numbers.append(line_no)

    print("Occurrences:", total)
    print("Line numbers:", line_numbers)
except FileNotFoundError:
    print("File not found.")
