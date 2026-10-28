filename = input("Enter filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    print("Total words:", len(text.split()))
except FileNotFoundError:
    print("File not found.")
