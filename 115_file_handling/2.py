filename = input("Enter filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
