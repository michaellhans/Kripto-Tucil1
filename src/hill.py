import string
import numpy as np

def encryptHillCipher(plaintext, kunci):
    '''
        plaintext: text yang ingin dienkripsi
        kunci: matrix m*m (simetri)
    '''
    m = len(kunci)
    # Jika pesan tidak dapat dibagi n, maka ditambah huruf random z
    while (len(plaintext)%m != 0):
        plaintext += "z"
    K = np.array(kunci)
    ciphertext = ''
    for i in range(0, len(plaintext), m):
        P = np.array([])
        for j in range(m):
            P = np.append(P, [string.ascii_lowercase.rfind(plaintext[i+j])])
        C = K.dot(P)
        for i in range(m):
            ciphertext += string.ascii_lowercase[int(C[i]) % 26]
    
    return ciphertext

def createDecryptKey(kunci):
    det = round(np.linalg.det(kunci)) % 26
    det_inv = -999
    for i in range(1,26):
        if ((det*i) % 26 == 1):
            det_inv = i
            break
    if (det_inv == -999):
        return Any, True
    Kinv = det_inv * np.linalg.det(kunci) * np.linalg.inv(kunci)
    
    return Kinv.round() % 26, False

def decryptHillCipher(ciphertext, kunci):
    '''
        plaintext: text yang ingin dienkripsi
        kunci: matrix m*m (simetri)
    '''
    m = len(kunci)
    K = np.array(kunci)
    Kinv, flag = createDecryptKey(K)
    if (flag):
        return 'Tidak dapat menemukan matrix dekripsi'
    plaintext = ''
    for i in range(0, len(ciphertext), m):
        P = np.array([])
        for j in range(m):
            P = np.append(P, [string.ascii_lowercase.rfind(ciphertext[i+j])])
        C = Kinv.dot(P)
        for i in range(m):
            plaintext += string.ascii_lowercase[int(C[i]) % 26]
    
    return plaintext

# TEST AREA
kunci = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]
plaintext = "paymoremoney"
ciphertext = encryptHillCipher(plaintext, kunci)
print("plaintext: ", plaintext)
print("encrypt: ", ciphertext.upper())
print("decrypt: ", decryptHillCipher(ciphertext.lower(), kunci))