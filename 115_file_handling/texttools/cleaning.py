import re
def clean_text(text): return re.sub(r'\\s+', ' ', re.sub(r'[^\\w\\s]', '', text)).strip()
