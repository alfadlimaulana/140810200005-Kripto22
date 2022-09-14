def shift(method):
    text = input("\nMasukkan kata: ")
    key = int(input("Masukkan key: "))
    output = ''
    if method == 'enkripsi' :
        for char in text:
            if (char.isupper()) == True :
                output += chr((((ord(char)-65)+key)%26)+65)
            else :
                output += chr((((ord(char)-97)+key)%26)+97)
    elif method == 'dekripsi' :
        for char in text:
            if (char.isupper()) == True :
                output += chr((((ord(char)-65)-key)%26)+65)
            else :
                output += chr((((ord(char)-97)-key)%26)+97)
    else : 
        print("Metode yang tersedia hanya enkripsi dan dekripsi.")
        return
    
    return output

while True :
    print("========Menu========")
    print("1. Enkripsi\n2. Dekripsi\n3. Keluar")
    pilihan = input("Pilihan: ")

    if pilihan == '1':
        output = shift("enkripsi")
        break
    elif pilihan == '2':
        output = shift("dekripsi")
        break
    elif pilihan == '3':
        exit()
    else :
        print("\nInput tidak sesuai.\n")
    
print("\nCiphertext: " + output)