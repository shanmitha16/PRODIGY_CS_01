def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

# Get text and shift value from the user
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))

# Encrypt the text using Caesar Cipher
encrypted_text = caesar_cipher(text, shift)
print("Encrypted:", encrypted_text)

# Decrypt the encrypted text
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted:", decrypted_text)
