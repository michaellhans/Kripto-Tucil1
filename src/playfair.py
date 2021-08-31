import string
import numpy as np

def processPlainText(plaintext):
    ''' Memproses plaintext '''
    # 1. ganti huruf j dengan i
    plaintext = plaintext.replace("j", "i")
    # 2. buat jadi bigram
    bigram_list = []
    i = 0
    while (i<len(plaintext)-1):
        if (plaintext[i] == plaintext[i+1]):
            # 3. sisip x pada pasangan huruf sama
            bigram_list.append(plaintext[i]+"x")
            # 4. huruf ganjil tambah x di akhir
            if (len(plaintext)%2 == 0):
                plaintext += "x"
            i += 1
        bigram_list.append(plaintext[i]+plaintext[i+1])
        i += 2

    return bigram_list

def processKey(kunci):
    ''' Memproses key '''
    # 1. Buang j dan huruf yang berulang
    kunci = kunci.lower().replace("j", "")
    kunci = ''.join(sorted(set(kunci), key=kunci.index))
    # 2. Tambah huruf yang belum ada selain j
    for char in string.ascii_lowercase.replace("j", ""):
        if char not in kunci:
            kunci += char
    # 3. Masukkan ke bujur sangkar
    mat = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(kunci[5*i + j])
        mat.append(row)

    return np.array(mat)

def encryptPlayfairCipher(plaintext, kunci):
    bigram = processPlainText(plaintext)
    kunci = processKey(kunci)
    ciphertext = ''
    for item in bigram:
        cipher1, cipher2 = '',''
        x1, y1 = np.where(kunci==item[0])
        x2, y2 = np.where(kunci==item[1])
        # 1. dua huruf terdapat pada baris kunci yang sama
        if (int(x1) == int(x2)):
            cipher1 = kunci[int(x1)][(int(y1)+1) % 5]
            cipher2 = kunci[int(x2)][(int(y2)+1) % 5]
        # 2. dua huruf terdapat pada kolom kunci yang sama
        elif (int(y1) == int(y2)):
            cipher1 = kunci[(int(x1)+1) % 5][int(y1)]
            cipher2 = kunci[(int(x2)+1) % 5][int(y2)]
        # 3. dua huruf tidak pada baris atau kolom yang sama
        else:
            cipher1 = kunci[int(x1)][int(y2)]
            cipher2 = kunci[int(x2)][int(y1)]
        
        ciphertext += (cipher1+cipher2)
    
    return ciphertext

def decryptPlayfairCipher(ciphertext, kunci):
    kunci = processKey(kunci)
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        plain1, plain2 = '',''
        x1, y1 = np.where(kunci==ciphertext[i])
        x2, y2 = np.where(kunci==ciphertext[i+1])
        # 1. dua huruf terdapat pada baris kunci yang sama
        if (int(x1) == int(x2)):
            plain1 = kunci[int(x1)][(int(y1)-1) % 5]
            plain2 = kunci[int(x2)][(int(y2)-1) % 5]
        # 2. dua huruf terdapat pada kolom kunci yang sama
        elif (int(y1) == int(y2)):
            plain1 = kunci[(int(x1)-1) % 5][int(y1)]
            plain2 = kunci[(int(x2)-1) % 5][int(y2)]
        # 3. dua huruf tidak pada baris atau kolom yang sama
        else:
            plain1 = kunci[int(x1)][int(y2)]
            plain2 = kunci[int(x2)][int(y1)]
        
        plaintext += (plain1+plain2)
    
    return plaintext.replace('x','')

# TEST AREA
plaintext = "temuiibunantimalam"
key = "JALANGANESHASEPULUH"
ciphertext = encryptPlayfairCipher(plaintext, key).upper()
print("plaintext: ", plaintext)
print("encrypt: ", ciphertext)
print("decrypt: ", decryptPlayfairCipher(ciphertext.lower(), key))