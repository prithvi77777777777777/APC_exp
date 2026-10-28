filename = input("Enter filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    print("Total characters (including spaces):", len(text))
except FileNotFoundError:
    print("File not found.")
