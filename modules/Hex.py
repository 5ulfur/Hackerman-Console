from utils import inputMultipleLines, clear, pause, Back, Style

def encode(plaintext):
    return plaintext.encode("UTF-8").hex()

def decode(ciphertext):
    return bytes.fromhex(ciphertext).decode("UTF-8")

def menu():
    while True:
        clear()
        print("Hex:")
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
