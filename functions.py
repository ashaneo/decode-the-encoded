# @title Default title text
def encode_caesar_cipher(text, shift=3):
    encoded_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shift_amount = shift % 26  # To handle shifts larger than the alphabet
            if char.islower():
                # Compute shift for lowercase letters
                shifted = ord(char) + shift_amount
                if shifted > ord('z'):
                    shifted -= 26
                encoded_text += chr(shifted)
            elif char.isupper():
                # Compute shift for uppercase letters
                shifted = ord(char) + shift_amount
                if shifted > ord('Z'):
                    shifted -= 26
                encoded_text += chr(shifted)
        else:
            # Add the character as is if it's not an alphabet letter
            encoded_text += char
    return encoded_text


def decode_caesar_cipher(encoded_text, shift=3):
    decoded_text = ""
    for char in encoded_text:
        if char.isalpha():  # Check if the character is an alphabet
            shift_amount = shift % 26  # To handle shifts larger than the alphabet
            if char.islower():
                # Compute shift back for lowercase letters
                shifted = ord(char) - shift_amount
                if shifted < ord('a'):
                    shifted += 26
                decoded_text += chr(shifted)
            elif char.isupper():
                # Compute shift back for uppercase letters
                shifted = ord(char) - shift_amount
                if shifted < ord('A'):
                    shifted += 26
                decoded_text += chr(shifted)
        else:
            # Add the character as is if it's not an alphabet letter
            decoded_text += char
    return decoded_text
