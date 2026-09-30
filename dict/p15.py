# Q15. Accept a sentence and create a dictionary containing each word and the number of times it occurs.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency:")
for key, value in frequency.items():
    print(key, "->", value)