# A library for the calculator modules to call upon for quick, common and helpful functions.
import os
from time import sleep

def is_valid(ii, mode):
    while True:
        try:
            if mode == "float":
                ii = float(ii) 
                break
            elif mode == "int":
                ii = int(ii)
                break
        except (ValueError, TypeError):
            ii = input("[!] Invalid input. Try again.\n> ")
    return ii

def show_menu(mm):
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(mm)
