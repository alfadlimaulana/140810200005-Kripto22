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

def hill(method):
    n = int(input("Masukkan ukuran matrix (n x n): "))
    
    key = list(map(in_range_number, input("Masukkan nilai key matrix (dipisahkan spasi): ").split()))
    key = np.array(key).reshape(n, n)
    
    print("Key Matrix: ")
    print(key)
    
    key_det = np.linalg.det(key)
    
    if key_det % 2 == 0 or key_det == 13 :
        print("Determinan matrix key harus ganjil selain 13")
        return
    
    text = input("\nMasukkan kata: ")
    if(len(text) < n) :
        print("n harus bilangan prima terkecil sebagai faktor dari jumlah karakter")
        return
    text = text.upper()
    print("Plaintext: " + text)
    
    if(len(text) % n != 0) :
        last_char = text[-1]
        text = last_char*(n - len(text) % n)
        
    text_in_number = list(map(char_to_number, list(text)))
    text_vector = np.array(text_in_number).reshape(int(len(text)/n), n)
    print("text vector: ")
    print(text_vector)
    
    result = np.array([], dtype=int)
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

    if pilihan == '1':
        output = hill("enkripsi")
        print("\nCiphertext: " + output)
        break
    elif pilihan == '2':
        output = hill("dekripsi")
        print("\Plaintext: " + output)
        break
    elif pilihan == '3':
        exit()
    else :
        print("\nInput tidak sesuai.\n")
    
