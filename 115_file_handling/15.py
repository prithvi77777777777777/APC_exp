import re

source = input("Enter Python source filename: ")
destination = input("Enter output filename: ")

try:
    with open(source, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Removes full-line comments; regex does not reliably parse # inside all string literals.
    cleaned = [line for line in lines if not re.match(r"^\\s*#", line)]

    with open(destination, "w", encoding="utf-8") as file:
        file.writelines(cleaned)

    print("Output saved to", destination)
except FileNotFoundError:
    print("Source file not found.")
