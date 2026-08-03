sentence = input("Enter a sentence: ")
result = []
for word in sentence.split():
    result.append(word[0].upper() + word[1:].lower())
print("Title case:", " ".join(result))
