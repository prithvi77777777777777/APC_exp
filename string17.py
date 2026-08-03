first = input("Enter the first string: ").replace(" ", "").lower()
second = input("Enter the second string: ").replace(" ", "").lower()
if sorted(first) == sorted(second):
    print("Anagrams")
else:
    print("Not anagrams")
