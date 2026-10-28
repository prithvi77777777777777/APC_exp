source = input("Enter source filename: ")
destination = input("Enter output filename: ")

try:
    with open(source, "r", encoding="utf-8") as file:
        text = file.read()

    with open(destination, "w", encoding="utf-8") as file:
        file.write(text.upper())

    print("Uppercase copy saved to", destination)
except FileNotFoundError:
    print("Source file not found.")
