from typing import Any
import string

def encryptAffineCipher(plaintext, n, m, b):
    '''
        plaintext: teks yang ingin di enkripsi
        n: ukuran alfabet
        m: bilangan bulat yang relatif prima dengan n
        b: jumlah pergeseran
    '''
    cipher = ""
    for letter in plaintext:
        p_pos = string.ascii_lowercase.rfind(letter)
        c = (m*p_pos + b) % n
        cipher += string.ascii_lowercase[c]
    return cipher

def getInversion(n, m):
    # cari inversi m (mod n)   
    for i in range(1,n):
        if ((m*i) % n == 1):
            return i, True
    
    # tidak ditemukan
    return Any, False

def decryptAffineCipher(ciphertext, n, m, b):
    '''
        ciphertext: teks yang ingin di dekripsi
        n: ukuran alfabet
        m: bilangan bulat yang relatif prima dengan n
        b: jumlah pergeseran
    '''
    m_inv, flag = getInversion(n, m)
    if flag:
        plain = ""
        for letter in ciphertext:
            c_pos = string.ascii_lowercase.rfind(letter)
            c = (m_inv*(c_pos - b)) % n
            plain += string.ascii_lowercase[c]
        return plain
    else:
        return str(m) + " tidak relatif prima dengan " + str(n)

# TEST SECTION
n, m, b = 26, 7, 10
plaintext = "kripto"
ciphertext = encryptAffineCipher(plaintext, n, m, b)

print("plaintext:", plaintext)
print("encrypt:", ciphertext.upper())
print("decrypt:", decryptAffineCipher(ciphertext, n, m, b))