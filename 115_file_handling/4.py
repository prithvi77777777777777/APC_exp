filename = input("Enter filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())
except FileNotFoundError:
    print("File not found.")
