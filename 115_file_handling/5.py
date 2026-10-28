filename = input("Enter filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        print("Total lines:", sum(1 for line in file))
except FileNotFoundError:
    print("File not found.")
