from utils import inputMultipleLines, clear, pause, Back, Style

def encrypt(plaintext, key):
    result = ""
    for c in plaintext:
        if c.isupper():
            result += chr((ord(c) + key - 65) % 26 + 65)
        elif c.islower():
            result += chr((ord(c) + key - 97) % 26 + 97)
        else:
            result += c
    return result

def decrypt(ciphertext, key):
    result = ""
    for c in ciphertext:
        if c.isupper():
            result += chr((ord(c) - key - 65) % 26 + 65)
        elif c.islower():
            result += chr((ord(c) - key - 97) % 26 + 97)
        else:
            result += c
    return result
    
def bruteforce(ciphertext):
    for i in range(1, 26):
        print("Key: " + str(i))
        print(Back.GREEN + decrypt(ciphertext, i) + Style.RESET_ALL + "\n")

def menu():
    while True:
        clear()
        print("Caesar Cipher:")
        print("\t1) Encrypt")
        print("\t2) Decrypt")
        print("\t3) Bruteforce")
        print("\t99) Return")
        select = input("Select: ")
        if select == "1":
            print("Plaintext (CTRL-D (UNIX) or CTRL-Z (Windows) to end): ")
            plaintext = inputMultipleLines()
            key = int(input("Key: "))
            print("\n" + Back.GREEN + encrypt(plaintext, key) + Style.RESET_ALL + "\n")
        elif select == "2":
            print("Ciphertext (CTRL-D (UNIX) or CTRL-Z (Windows) to end): ")
            ciphertext = inputMultipleLines()
            key = int(input("Key: "))
            print("\n" + Back.GREEN + decrypt(ciphertext, key) + Style.RESET_ALL + "\n")
        elif select == "3":
            print("Ciphertext (CTRL-D (UNIX) or CTRL-Z (Windows) to end): ")
            ciphertext = inputMultipleLines()
            bruteforce(ciphertext)
        elif select == "99":
            break
        pause()
