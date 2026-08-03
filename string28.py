paragraph = input("Enter a paragraph: ").lower()
frequency = {}
for word in paragraph.split():
    word = word.strip(".,!?;:\"'()[]{}")
    if word:
        frequency[word] = frequency.get(word, 0) + 1
for word, count in frequency.items():
    print(word, ":", count)
