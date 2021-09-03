import string, re

def preprocessPlainText(plaintext):
    # remove digit
    remove_digit = str.maketrans('','', string.digits)
    plaintext = plaintext.translate(remove_digit)

    # remove enter and whitespace
    plaintext = plaintext.replace("\n", "")
    plaintext = plaintext.replace(" ", "")

    # remove tanda baca
    plaintext = re.sub(r'[^\w\s]', '', plaintext)
    
    return plaintext

def showPerFive(ciphertext):
    ciphertext.upper()
    cipher_list = [ciphertext[idx: idx+5] for idx in range(0, len(ciphertext), 5)]
    return " ".join(cipher_list)

def saveCiphertext(ciphertext, filename):
    file = open("../saved file/"+filename+".txt", "w")
    file.write(ciphertext)
    file.close()

# Unit Testing
if __name__ == "__main__":
    # plaintext = "!abc\n123  d.e,f345 gh\ni?"
    # print("was:", plaintext)
    # print("then:", preprocessPlainText("!abc\n123  d.e,f345 ghi?"))
    # print(showPerFive("ABCDEFGHIJK"))
    saveCiphertext("SKAWNUR", "affine")