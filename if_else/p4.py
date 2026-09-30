# Q4. Write a PYTHON program to check entered character is vowel or consonant.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

ch = input("Enter a character: ").lower()

if ch in ('a', 'e', 'i', 'o', 'u'):
    print("The character is a VOWEL")
else:
    print("The character is a CONSONANT")