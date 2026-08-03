text = input("Enter a string: ")
frequency = {}
for character in text:
    frequency[character] = frequency.get(character, 0) + 1
if len(frequency) < 2:
    print("A second most frequent character does not exist.")
else:
    ordered = sorted(frequency, key=frequency.get, reverse=True)
    print("Second most frequent character:", ordered[1])
