text = input("Enter a string: ")
compressed = ""
if text:
    count = 1
    for index in range(1, len(text)):
        if text[index] == text[index - 1]:
            count += 1
        else:
            compressed += text[index - 1] + str(count)
            count = 1
    compressed += text[-1] + str(count)
print("Compressed string:", compressed if len(compressed) < len(text) else text)
