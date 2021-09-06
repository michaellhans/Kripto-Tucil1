# default_full.py
# Contain all default and full Vigenere Ciphere encryption and decryption algorithm
# Difference between default and full vigenere: The cipher matrix

from vigenere_support import alpha_to_int, int_to_alpha, default_cipher_matrix, full_cipher_matrix

def vigenere_cipher(plain_text, key, cipher_matrix=default_cipher_matrix):
    '''
    Encrypt plain text with default or full vigenere cipher algorithm
    Depends on which cipher matrix is used in the algorithm
    '''
    cipher_text = ""
    n = len(plain_text)
    key_length = len(key)
    i = 0
    j = 0
    while (i < n):
        if (j == key_length):
            j = 0
        row = alpha_to_int[key[j]]
        col = alpha_to_int[plain_text[i]]
        cipher_text += cipher_matrix[row][col]
        j += 1
        i += 1
    return cipher_text

def decrypt_vigenere_cepher(cipher_text, key, cipher_matrix=default_cipher_matrix):
    '''
    Decrypt cipher text with default or full vigenere cipher algorithm
    Depends on which cipher matrix is used in the algorithm
    '''
    plain_text = ""
    n = len(cipher_text)
    key_length = len(key)
    i = 0
    j = 0
    while (i < n):
        if (j == key_length):
            j = 0
        row = alpha_to_int[key[j]]
        plain_char = int_to_alpha[cipher_matrix[row].index(cipher_text[i])]
        plain_text += plain_char
        j += 1
        i += 1
    return plain_text

# Unit Testing
if __name__ == "__main__":
    key = "SONY"
    plain_text = "THISPLAINTEXT"

    print("1. Vigenere Cipher")
    cipher_text = vigenere_cipher(plain_text, key)
    print("Plain text\t:", plain_text)
    print("Cipher text\t:", cipher_text)
    print("Decrypted text\t:",decrypt_vigenere_cepher(cipher_text, key))

    print("\n2a. Full Vigenere Cipher")
    cipher_text = vigenere_cipher(plain_text, key, full_cipher_matrix)
    print("Plain text\t:", plain_text)
    print("Cipher text\t:", cipher_text)
    print("Decrypted text\t:",decrypt_vigenere_cepher(cipher_text, key, full_cipher_matrix))