from itertools import zip_longest

first = input("Enter first filename: ")
second = input("Enter second filename: ")

try:
    with open(first, "r", encoding="utf-8") as file:
        lines1 = file.readlines()
    with open(second, "r", encoding="utf-8") as file:
        lines2 = file.readlines()

    if lines1 == lines2:
        print("Files are identical.")
    else:
        print("Files are different.")
        for line_no, (a, b) in enumerate(zip_longest(lines1, lines2, fillvalue=None), start=1):
            if a != b:
                print("First difference at line", line_no)
                print("First file:", repr(a))
                print("Second file:", repr(b))
                break
except FileNotFoundError:
    print("One of the files was not found.")
