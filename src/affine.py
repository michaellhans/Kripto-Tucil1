from typing import Any

def encryptAffineCipher(plaintext, n, m, b):
    '''
        plaintext: teks yang ingin di enkripsi
        n: ukuran alfabet
        m: bilangan bulat yang relatif prima dengan n
        b: jumlah pergeseran
    '''
    #TODO handle tanda baca, spasi, angka (selain 26 alphabet)
    cipher = ""
    for letter in plaintext:
        base = "a"
        if letter.isupper():
            base = "A"
        
        p_ord = ord(letter) - ord(base)
        c = (m*p_ord + b) % n
        c_ord = c + ord(base)

        cipher += chr(c_ord)
    return cipher

def getInversion(n, m):
    # cari inversi m (mod n)   
    for i in range(1,n):
        if ((m % n)*(i % n) % n == 1):
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
            base = "a"
            if letter.isupper():
                base = "A"
            
            c_ord = ord(letter) - ord(base)
            c = (m_inv*(c_ord - b)) % n
            p_ord = c + ord(base)

            plain += chr(p_ord)
        return plain
    else:
        return str(m) + " tidak relatif prima dengan " + str(n)

# TEST SECTION
n, m, b = 26, 7, 10
plaintext = "KriptO"
ciphertext = encryptAffineCipher(plaintext, n, m, b)

print("plaintext:", plaintext)
print("encrypt:", ciphertext)
print("decrypt:", decryptAffineCipher(ciphertext, n, m, b))