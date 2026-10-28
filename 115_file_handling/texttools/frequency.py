from collections import Counter
def word_frequency(text): return dict(Counter(word.lower() for word in text.split()))
