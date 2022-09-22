import numpy as np

def in_range_number(x):
    x = int(x)
    return x % 26

def char_to_number(x):
    x = ord(x)-65
    return x

def number_to_char(x):
    x = chr(x+65)
    return x

def mod_inverse(A, M):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

def input_key(n):
    key = list(map(in_range_number, input("Masukkan nilai key matrix (dipisahkan spasi): ").split()))
    key = np.array(key).reshape(n, n)
    
    print("Key Matrix: ")
    print(key)
    
    return key

def input_text():
    text = input("\nMasukkan kata: ")
    ' '.join(text)
    text = text.upper()
    
    return text

def hill(method, text, key):    
    key_det = np.linalg.det(key) % 26
    
    if key_det % 2 == 0 or key_det == 13 :
        print("Determinan matrix key harus ganjil selain 13")
        return
    
    if(len(text) % n != 0) :
        last_char = text[-1]
        text = last_char*(n - len(text) % n)
        
    text_in_number = list(map(char_to_number, list(text)))
    text_vector = np.array(text_in_number).reshape(int(len(text)/n), n)
    
    result = np.array([], dtype=int)
 
    if method == 'dekripsi':
        det_inverse = mod_inverse(key_det, 26)
        key = (
            det_inverse * np.round(key_det * np.linalg.inv(key)).astype(int) % 26
        )

    for i in range(len(text_vector)):
            temp = np.matmul(key, text_vector[i].reshape(n, 1)) % 26
            result = np.append(result, temp)
    result = list(map(number_to_char, result))
        
    output = ''.join(result)
    
    return output


while True :
    print("========Menu========")
    print("1. Enkripsi\n2. Dekripsi\n3. Keluar")
    pilihan = input("Pilihan: ")

    n = int(input("\nMasukkan ukuran key matrix (n x n): "))
    key = input_key(n)
    
    text = ''
    while(len(text) < n):
        text = input_text()
        if(len(text) < n):
            print("n harus bilangan prima terkecil sebagai faktor dari jumlah karakter")
            
    if pilihan == '1':
        print("\nPlaintext: " + text)
        output = hill("enkripsi", text, key)
        print("Ciphertext: " + output)
        break
    elif pilihan == '2':
        print("\nCiphertext: " + text)
        output = hill("dekripsi", text, key)
        print("Plaintext: " + output)
        break
    elif pilihan == '3':
        exit()
    else :
        print("\nInput tidak sesuai.\n")
    
