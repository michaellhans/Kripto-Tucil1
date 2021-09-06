# vigenere_support.py
# Support all vigenere algorithm such as all general maps and cipher matrix

import random

def get_all_alphabet():
    '''
    Generate list of alphabet
    '''
    basis_val = 65
    arr = []
    for i in range(26):
        arr.append(chr(basis_val + i))
    return arr

def int_to_alpha_map():
    '''
    Generate map<int, alphabet> for extended vigenere cipher purpose
    '''
    int_to_alpha = {}
    basis_val = 65
    for i in range(26):
        int_to_alpha.update({i: chr(basis_val + i)})
    return int_to_alpha

def alpha_to_int_map():
    '''
    Generate map<alphabet, int> for extended vigenere cipher purpose
    '''
    alpha_to_int = {}
    basis_val = 65
    for i in range(26):
        alpha_to_int.update({chr(basis_val + i): i})
    return alpha_to_int

def generate_cipher_matrix():
    '''
    Generate default cipher matrix for default viginere ciphere purpose
    '''
    mat = []
    for i in range (26):
        row = []
        for j in range(26):
            ascii_val = (i+j) % 26
            row.append(int_to_alpha[ascii_val])
        mat.append(row)
    return mat

def generate_full_cipher_matrix():
    '''
    Generate full cipher matrix for full viginere ciphere purpose
    Assume the permutation depends on the seed from 1 to 26
    '''
    mat = []
    all_alphabet = get_all_alphabet()
    for i in range (26):
        random.seed(i)
        row = random.sample(all_alphabet, len(all_alphabet))
        mat.append(row)
    return mat

# Four global variable to support default and full extended vigenere
int_to_alpha = int_to_alpha_map()
alpha_to_int = alpha_to_int_map()
default_cipher_matrix = generate_cipher_matrix()
full_cipher_matrix = generate_full_cipher_matrix()

def int_to_ascii_map():
    '''
    Generate map<int, ascii> for extended vigenere cipher purpose
    '''
    int_to_ascii = {}
    for i in range(256):
        int_to_ascii.update({i: chr(i)})
    return int_to_ascii

def ascii_to_int_map():
    '''
    Generate map<ascii, int> for extended vigenere cipher purpose
    '''
    ascii_to_int = {}
    for i in range(256):
        ascii_to_int.update({chr(i): i})
    return ascii_to_int

def generate_ascii_cipher_matrix():
    '''
    Generate ascii_cipher_matrix for extended vigenere cipher purpose
    '''
    mat = []
    for i in range (256):
        row = []
        for j in range(256):
            ascii_val = (i+j) % 256
            row.append(int_to_ascii[ascii_val])
        mat.append(row)
    return mat

# Three global variable to support extended vigenere
int_to_ascii = int_to_ascii_map()
ascii_to_int = ascii_to_int_map()
ascii_cipher_matrix = generate_ascii_cipher_matrix()