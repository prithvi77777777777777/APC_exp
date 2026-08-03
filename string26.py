def caesar_cipher(text, shift):
    result = ""
    for character in text:
        if character.isalpha():
            base = ord("A") if character.isupper() else ord("a")
            result += chr((ord(character) - base + shift) % 26 + base)
        else:
            result += character
    return result


message = input("Enter a message: ")
shift = int(input("Enter shift value: "))
encrypted = caesar_cipher(message, shift)
print("Encrypted:", encrypted)
print("Decrypted:", caesar_cipher(encrypted, -shift))
