# Q18. Accept a sentence from the user and use a set to display all unique words.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

sentence = input("Enter a sentence: ")

words = sentence.split()
unique_words = set(words)

print("Unique Words:", unique_words)