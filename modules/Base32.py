from utils import inputMultipleLines, clear, pause, Back, Style
from base64 import b32encode, b32decode

def encode(plaintext):
    return b32encode(plaintext.encode('UTF-8')).decode('UTF-8')

def decode(ciphertext):
    return b32decode(ciphertext).decode('UTF-8')

def menu():
    while True:
        clear()
        print("Base32:")
        print("\t1) Encode")
        print("\t2) Decode")
        print("\t99) Return")
        select = input("Select: ")
        if select == "1":
            print("Plaintext (CTRL-D (UNIX) or CTRL-Z (Windows) to end): ")
            plaintext = inputMultipleLines()
            print("\n" + Back.GREEN + encode(plaintext) + Style.RESET_ALL + "\n")
        elif select == "2":
            ciphertext = input("Ciphertext: ")
            try:
                print("\n" + Back.GREEN + decode(ciphertext) + Style.RESET_ALL + "\n")
            except:
                print("\n" + Back.RED + "Invalid character" + Style.RESET_ALL + "\n")
        elif select == "99":
            break
        pause()
