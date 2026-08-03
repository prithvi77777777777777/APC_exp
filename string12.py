sentence = input("Enter a sentence: ")
words = sentence.split()
if words:
    print("Longest word:", max(words, key=len))
else:
    print("No words entered.")
