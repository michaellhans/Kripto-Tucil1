# Vigenere Cipher

import random

def get_all_alphabet():
    basis_val = 65
    arr = []
    for i in range(26):
        arr.append(chr(basis_val + i))
    return arr

def generate_ascii_char():
    int_to_ascii_char = {}
    for i in range(256):
        int_to_ascii_char.update({i: chr(i)})
    return int_to_ascii_char

def generate_ascii_integer():
    ascii_to_int = {}
    for i in range(26):
        ascii_to_int.update({chr(i): i})
    return ascii_to_int

def generate_alphabet():
    int_to_alpha = {}
    basis_val = 65
    for i in range(26):
        int_to_alpha.update({i: chr(basis_val + i)})
    return int_to_alpha

def generate_integer():
    alpha_to_int = {}
    basis_val = 65
    for i in range(26):
        alpha_to_int.update({chr(basis_val + i): i})
    return alpha_to_int

def generate_full_cipher_matrix():
    mat = []
    all_alphabet = get_all_alphabet()
    for i in range (26):
        row = random.sample(all_alphabet, len(all_alphabet))
        print(row)
        mat.append(row)
    return mat

def generate_cipher_matrix():
    mat = []
    for i in range (26):
        row = []
        for j in range(26):
            ascii_val = (i+j) % 26
            row.append(int_to_alpha[ascii_val])
        mat.append(row)
    return mat

def generate_ascii_cipher_matrix():
    mat = []
    for i in range (256):
        row = []
        for j in range(256):
            ascii_val = (i+j) % 256
            row.append(int_to_ascii_char[ascii_val])
        mat.append(row)
    return mat

int_to_ascii_char = generate_ascii_char()
int_to_alpha = generate_alphabet()
alpha_to_int = generate_integer()
ascii_char_to_int = generate_ascii_integer()
default_cipher_matrix = generate_cipher_matrix()
ascii_cipher_matrix = generate_ascii_cipher_matrix()
full_cipher_matrix = generate_full_cipher_matrix()

for row in ascii_cipher_matrix:
    for value in row:
        print(value, end=" ")
    print()

def vigenere_cipher(plain_text, key, cipher_matrix=default_cipher_matrix):
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

def auto_key_vigenere_cipher(plain_text, key, cipher_matrix=default_cipher_matrix):
    cipher_text = ""
    n = len(plain_text)
    key_length = len(key)
    key_stream = key + plain_text[:n - key_length]
    i = 0
    while (i < n):
        row = alpha_to_int[key_stream[i]]
        col = alpha_to_int[plain_text[i]]
        cipher_text += cipher_matrix[row][col]
        i += 1
    return cipher_text

def decrypt_auto_key_vigenere_cepher(cipher_text, key, cipher_matrix=default_cipher_matrix):
    plain_text = ""
    n = len(cipher_text)
    key_length = len(key)
    key_stream = key
    i = 0
    while (i < n):
        row = alpha_to_int[key_stream[i]]
        plain_char = int_to_alpha[cipher_matrix[row].index(cipher_text[i])]
        plain_text += plain_char
        if (i + key_length < n):
            key_stream += plain_char
        i += 1
    return plain_text

def extended_vigenere_cipher(plain_text, key, cipher_matrix=ascii_cipher_matrix):
    cipher_text = ""
    n = len(plain_text)
    key_length = len(key)
    i = 0
    j = 0
    while (i < n):
        if (j == key_length):
            j = 0
        row = int_to_ascii_char[key[j]]
        col = int_to_ascii_char[plain_text[i]]
        cipher_text += cipher_matrix[row][col]
        j += 1
        i += 1
    return cipher_text

def decrypt_extended_vigenere_cepher(cipher_text, key, cipher_matrix=ascii_cipher_matrix):
    plain_text = ""
    n = len(cipher_text)
    key_length = len(key)
    i = 0
    j = 0
    while (i < n):
        if (j == key_length):
            j = 0
        row = ascii_char_to_int[key[j]]
        plain_char = int_to_ascii_char[cipher_matrix[row].index(cipher_text[i])]
        plain_text += plain_char
        j += 1
        i += 1
    return plain_text

key = "SONY"
plain_text = "THISPLAINTEXT"

print("\nVigenere Cipher")
cipher_text = vigenere_cipher(plain_text, key)
print(cipher_text)
print(decrypt_vigenere_cepher(cipher_text, key))

print("\nAuto Key Vigenere Cipher")
cipher_text = auto_key_vigenere_cipher(plain_text, key)
print(cipher_text)
print(decrypt_auto_key_vigenere_cepher(cipher_text, key))

print("\nFull Vigenere Cipher")
cipher_text = vigenere_cipher(plain_text, key, full_cipher_matrix)
print(cipher_text)
print(decrypt_vigenere_cepher(cipher_text, key, full_cipher_matrix))

print("\nFull and Auto Key Vigenere Cipher")
cipher_text = auto_key_vigenere_cipher(plain_text, key, full_cipher_matrix)
print(cipher_text)
print(decrypt_auto_key_vigenere_cepher(cipher_text, key, full_cipher_matrix))

print("\nFull Extended Vigenere Cipher")
cipher_text = vigenere_cipher(plain_text, key, ascii_cipher_matrix)
print(cipher_text)
print(decrypt_vigenere_cepher(cipher_text, key, ascii_cipher_matrix))