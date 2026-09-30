# Q35. Accept a paragraph and create a dictionary where Key = word length, Value = number of words having that length.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

paragraph = input("Enter a paragraph: ")

words = paragraph.split()
length_count = {}

for word in words:
    length = len(word)
    if length in length_count:
        length_count[length] += 1
    else:
        length_count[length] = 1

print("\nWords in Paragraph:", words)
print("\nWord Length Frequency:")
for length in sorted(length_count.keys()):
    print("Length", length, "->", length_count[length], "word(s)")