import re

source_file = input("Enter source filename: ")
old_word = input("Word to replace: ")
new_word = input("Replacement word: ")
output_file = input("Output filename (enter same filename to overwrite): ")

try:
    with open(source_file, "r", encoding="utf-8") as file:
        text = file.read()

    updated = re.sub(r"\\b" + re.escape(old_word) + r"\\b",
                     lambda match: new_word, text, flags=re.IGNORECASE)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(updated)

    print("Updated text saved to", output_file)
except FileNotFoundError:
    print("Source file not found.")
