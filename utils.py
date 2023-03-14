import os
import colorama
from colorama import Fore, Back, Style

colorama.init(convert=True)

def inputMultipleLines():
    result = ""
    while True:
        try:
            line = input()
        except EOFError:
            result = result[:-1]
            break
        result += line + "\n"
    return result

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def pause():
    os.system("pause")
