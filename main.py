from utils import clear
import importlib
from os import listdir
from os.path import isfile, join

modules_path = "modules"
modules = [".".join(file.split(".")[:-1]) for file in listdir(modules_path) if isfile(join(modules_path, file))]

def banner():
    print(" ____________________________________________________________________________")
    print("|  _   _   _____   ____   _  __  ____   _____   ___  ___   _____   ___    _  |")
    print("| | |_| | |  _  | |  __| | |/ / |  __| |  _  | |   \/   | |  _  | |   \  | | |")
    print("| |  _  | | |_| | | |    |   /  | |_   | |_| | | |\  /| | | |_| | | |\ \ | | |")
    print("| | | | | |  _  | | |__  | | \  |  _|  |    _| | | \/ | | |  _  | | | \ \| | |")
    print("| |_| |_| |_| |_| |____| |_|\_\ |____| |_|\_\  |_|    |_| |_| |_| |_|  \___| |")
    print("|____________________________________________________________________________|")

def menu():
    while True:
        clear()
        banner()
        for i in range(len(modules)):
            print(f"\t{i}) {modules[i]}")
        print("\t99) Exit")
        try:
            select = int(input("Select: "))
            if select == 99:
                break
            module = importlib.import_module(f"{modules_path}.{modules[select]}")
            module.menu()
        except:
            continue
        
if __name__ == "__main__":
    menu()
