sentence = input("Enter a sentence: ")
word = input("Enter a word to count: ")
count = 0
for item in sentence.split():
    if item.strip(".,!?;:").lower() == word.lower():
        count += 1
print("Occurrences:", count)
