# util.py
# All utilization such as load, save, and preprocessing are in this module

import string, re
import random

def preprocessPlainText(plaintext):
    '''
    Preprocess plain text (except for Extended Vigenere Ciphere)
    Remove all non-alphabet characters from the plaintext
    Return the new pre-processed plaintext
    '''
    # remove digit
    remove_digit = str.maketrans('','', string.digits)
    plaintext = plaintext.translate(remove_digit)

    # remove enter and whitespace
    plaintext = plaintext.replace("\n", "")
    plaintext = plaintext.replace(" ", "")

    # remove tanda baca
    plaintext = re.sub(r'[^\w\s]', '', plaintext)
    
    return plaintext.upper()

def showPerFive(ciphertext):
    '''
    Format the output cipher text with group of five characters mode
    '''
    ciphertext.upper()
    cipher_list = [ciphertext[idx: idx+5] for idx in range(0, len(ciphertext), 5)]
    return " ".join(cipher_list)

def saveOutputText(ciphertext, filename, encryption_mode, is_extended=False):
    '''
    Save the output text into the text file
    Can save ASCII characters (Extended Vigenere Ciphere only)
    '''
    # If the file is input from the text box
    if (filename == ""):
        filename = "test-" + str(random.randint(1, 1000)) + ".txt"
    
    # If the mode is in encryption mode
    if (encryption_mode):
        path = "../dump/encrypted/" + filename
    # Decryption mode
    else:
        path = "../dump/decrypted/" + filename + ".txt"

    # If the active ciphere type is Extended Vigenere Type, use encoding "latin-1"
    if (is_extended):
        with open(path, 'w', encoding="latin-1") as file:
            file.write(ciphertext)
    else:
        with open(path, 'w') as file:
            file.write(ciphertext)

def saveBinaryFile(ciphertext, filename, encryption_mode):
    '''
    Save the output binary into the binary file
    Can save ASCII characters (Extended Vigenere Ciphere only)
    '''
    # If the file is input from the text box
    if (filename == ""):
        filename = "test-" + str(random.randint(1, 1000)) + ".bin"
    
    # If the mode is in encryption mode
    if (encryption_mode):
        path = "../dump/encrypted/" + filename + ".bin"
    # Decryption mode
    else:
        path = "../dump/decrypted/" + filename[:-4]
    with open(path, 'w', encoding="latin-1") as file:
        file.write(ciphertext)

def readFile(path):
    '''
    Read the text-based file
    '''
    file = open(path, "r")
    return file.read()

def readBinary(path):
    '''
    Read the binary file
    '''
    file = open(path, "r", encoding="latin-1")
    return file.read()

# Unit Testing
if __name__ == "__main__":
    plaintext = "!abc\n123  d.e,f345 gh\ni?"
    print("was:", plaintext)
    print("then:", preprocessPlainText("!abc\n123  d.e,f345 ghi?"))
    print(showPerFive("ABCDEFGHIJK"))
    saveOutputText("SKAWNUR", "affine")