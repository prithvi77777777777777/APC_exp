# Q9. Create a dictionary of programming languages and their creators. Display each key and value using a loop.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich"
}

print("Programming Languages and their Creators:")
for lang, creator in languages.items():
    print(lang, "->", creator)