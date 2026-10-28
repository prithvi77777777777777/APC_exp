def count_vowels(text): return sum(ch.lower() in "aeiou" for ch in text)
def reverse_string(text): return text[::-1]
def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]
def count_words(text): return len(text.split())
def remove_spaces(text): return text.replace(" ", "")
