import string, re
import random

def preprocessPlainText(plaintext):
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
    ciphertext.upper()
    cipher_list = [ciphertext[idx: idx+5] for idx in range(0, len(ciphertext), 5)]
    return " ".join(cipher_list)

def saveOutputText(ciphertext, filename, mode):
    start_path = "../dump/encrypted/"
    if (mode == False):
        start_path = "../dump/decrypted/"
    if (filename == ""):
        filename = "test-" + str(random.randint(1, 1000))
    file = open(start_path + filename + ".txt", "w")
    file.write(ciphertext)
    file.close()

def saveBinaryFile(ciphertext, filename, mode):
    start_path = "../dump/encrypted/"
    if (mode == False):
        start_path = "../dump/decrypted/"
    if (filename == ""):
        filename = "test-" + str(random.randint(1, 1000))
    with open(start_path + filename + ".bin", 'w', encoding="latin-1") as file:
        file.write(ciphertext)

def readFile(path):
    file = open(path, "r")
    return file.read()

def readBinary(path):
    file = open(path, "r", encoding="latin-1")
    return file.read()

# Unit Testing
if __name__ == "__main__":
    # plaintext = "!abc\n123  d.e,f345 gh\ni?"
    # print("was:", plaintext)
    # print("then:", preprocessPlainText("!abc\n123  d.e,f345 ghi?"))
    # print(showPerFive("ABCDEFGHIJK"))
    saveOutputText("SKAWNUR", "affine")