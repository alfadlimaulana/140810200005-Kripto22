from numpy import number


def input_text(string):
    text = input("Masukkan " + string + ": ")
    text = text.replace(' ', '')
    
    return text

def char_to_number(char):
    number = 0
    if char.isupper():
        number = ord(char)-65
    elif char.islower():
        number = ord(char)-97
    return number

def number_to_char(number, isUpper):
    char = ''
    if isUpper:
        char = chr(number+65)
    else:
        char = chr(number+97)
    return char

def shift(text, method):
    key = input("Masukkan key: ").upper()
    long_key = key
    
    while (len(long_key) < len(text)):
        long_key += key
    
    if (len(long_key) > len(text)):
        n = len(text) - len(long_key)
        long_key = long_key[0:n]
        
    output = ''
    if method == 'enkripsi' :
        for i in range(len(text)):
            output += number_to_char((char_to_number(text[i]) + char_to_number(long_key[i])) % 26, text[i].isupper())
    elif method == 'dekripsi' :
        for i in range(len(text)):
            output += number_to_char((char_to_number(text[i]) - char_to_number(long_key[i])) % 26, text[i].isupper())
    else:
        print("Metode yang tersedia hanya enkripsi dan dekripsi.")
        return
    
    return output

while True :
    print("========Menu========")
    print("1. Enkripsi\n2. Dekripsi\n3. Keluar")
    pilihan = input("Pilihan: ")

    if pilihan == '1':
        plaintext = input_text("plaintext")
        output = shift(plaintext, "enkripsi")
        break
    elif pilihan == '2':
        ciphertext = input_text("ciphertext")
        output = shift(ciphertext, "dekripsi")
        break
    elif pilihan == '3':
        exit()
    else :
        print("\nInput tidak sesuai.\n")
    
print("\nCiphertext: " + output)