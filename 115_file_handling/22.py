first = input("Enter first filename: ")
second = input("Enter second filename: ")
output = input("Enter output filename: ")

try:
    with open(first, "r", encoding="utf-8") as file:
        text1 = file.read()
    with open(second, "r", encoding="utf-8") as file:
        text2 = file.read()

    with open(output, "w", encoding="utf-8") as file:
        file.write(text1)
        file.write("\\n")
        file.write(text2)

    print("Combined contents saved to", output)
except FileNotFoundError:
    print("One of the input files was not found.")
