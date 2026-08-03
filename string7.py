text = input("Enter a string: ")
result = ""
for character in text:
    if character != " ":
        result += character
print("Without spaces:", result)
