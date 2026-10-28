filename = input("Enter filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    print("Lines in reverse order:")
    for line in reversed(lines):
        print(line, end="")
except FileNotFoundError:
    print("File not found.")
