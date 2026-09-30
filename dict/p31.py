# Q31. Take a list of words, create a dictionary where the key is the word length and the value is a list of words having that length.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

words = ["apple", "bat", "cat", "mango", "dog", "kiwi", "orange"]

length_dict = {}

for word in words:
    length = len(word)
    if length in length_dict:
        length_dict[length].append(word)
    else:
        length_dict[length] = [word]

print("List of Words:", words)
print("\nWords Grouped by Length:")
for length, word_list in length_dict.items():
    print("Length", length, "->", word_list)