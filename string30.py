first = input("Enter the first string: ")
second = input("Enter the second string: ")
if len(first) == len(second) and second in (first + first):
    print("Yes, it is a rotation.")
else:
    print("No, it is not a rotation.")
