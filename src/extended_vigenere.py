# extended_vigenere.py
# Contain all Extended Vigenere Ciphere encryption and decryption algorithm

from vigenere_support import ascii_to_int, int_to_ascii, ascii_cipher_matrix

def extended_vigenere_cipher(plain_text, key, cipher_matrix=ascii_cipher_matrix):
    '''
    Encrypt plain text with extended vigenere cipher algorithm
    '''
    cipher_text = ""
    n = len(plain_text)
    key_length = len(key)
    i = 0
    j = 0
    while (i < n):
        if (j == key_length):
            j = 0
        row = ascii_to_int[key[j]]
        col = ascii_to_int[plain_text[i]]
        cipher_text += cipher_matrix[row][col]
        j += 1
        i += 1
    return cipher_text

def decrypt_extended_vigenere_cepher(cipher_text, key, cipher_matrix=ascii_cipher_matrix):
    '''
    Decrypt cipher text with extended vigenere cipher algorithm
    '''
    plain_text = ""
    n = len(cipher_text)
    key_length = len(key)
    i = 0
    j = 0
    while (i < n):
        if (j == key_length):
            j = 0
        row = ascii_to_int[key[j]]
        plain_char = int_to_ascii[cipher_matrix[row].index(cipher_text[i])]
        plain_text += plain_char
        j += 1
        i += 1
    return plain_text

# Unit Testing
if __name__ == "__main__":
    key = "0000"
    plain_text = "ABCDEFGHIJKL"

    print("3. Extended Vigenere Cipher")
    cipher_text = extended_vigenere_cipher(plain_text, key)
    print("Plain text\t:", plain_text)
    print("Cipher text\t:", cipher_text)
    print("Decrypted text\t:",decrypt_extended_vigenere_cepher(cipher_text, key))