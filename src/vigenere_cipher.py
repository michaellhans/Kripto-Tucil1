# Vigenere Cipher

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

def generate_cipher_matrix():
    mat = []
    for i in range (26):
        row = []
        for j in range(26):
            ascii_val = (i+j) % 26
            row.append(int_to_alpha[ascii_val])
        mat.append(row)
    return mat

int_to_alpha = generate_alphabet()
alpha_to_int = generate_integer()
cipher_matrix = generate_cipher_matrix()

def vigenere_cipher(plain_text, key):
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

key = "SONY"
plain_text = "THISPLAINTEXT"
print(vigenere_cipher(plain_text, key))


