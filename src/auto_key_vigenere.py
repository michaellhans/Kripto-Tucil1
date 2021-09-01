# Auto Key Vigenere Cipher

from vigenere_support import alpha_to_int, int_to_alpha, default_cipher_matrix

def auto_key_vigenere_cipher(plain_text, key, cipher_matrix=default_cipher_matrix):
    '''
    Encrypt plain text with auto key vigenere cipher algorithm
    Depends on which cipher matrix is used in the algorithm
    '''
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
    '''
    Decrypt cipher text with auto key vigenere cipher algorithm
    Depends on which cipher matrix is used in the algorithm
    '''
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

# Unit Testing
if __name__ == "__main__":
    key = "SONY"
    plain_text = "THISPLAINTEXT"

    print("2b. Auto-Key Vigenere Cipher")
    cipher_text = auto_key_vigenere_cipher(plain_text, key)
    print("Plain text\t:", plain_text)
    print("Cipher text\t:", cipher_text)
    print("Decrypted text\t:",decrypt_auto_key_vigenere_cepher(cipher_text, key))