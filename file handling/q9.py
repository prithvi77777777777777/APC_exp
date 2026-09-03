'''9.	Read a text file and count the number of vowels and consonants present in the file.'''

with open('student.txt', 'r') as file:
    content = file.read().lower()
    vowels=['a','e','i','o','u','A','E','I','O','U']
    vowel_count = 0
    consonant_count = 0
    for i in content:
        if i.isalpha():
            if i in vowels:
                vowel_count += 1
                print(i.upper(),end=' ')
            else:
                consonant_count += 1
                print(i,end=' ')
        else:
            print()
print(f"Total number of vowels in the file: {vowel_count}")
print(f"Total number of consonants in the file: {consonant_count}")