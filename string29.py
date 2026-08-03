sentence = input("Enter a sentence: ")
words = sentence.split()
result = ""
for word in words:
    result = word + (" " if result else "") + result
print("Reversed sentence:", result)
