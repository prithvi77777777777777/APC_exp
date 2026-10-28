from texttools.cleaning import clean_text
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency

text = input("Enter text: ")
cleaned = clean_text(text)
print("Cleaned:", cleaned)
print("Tokens:", tokenize(cleaned))
print("Frequency:", word_frequency(cleaned))
