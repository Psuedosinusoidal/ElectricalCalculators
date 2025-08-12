# A library for the calculator modules to call upon for quick, common and helpful functions.
import os
from time import sleep

def is_valid(*args):
    try:
        ii = args[0]
        mode = args[1]
        if mode == "float":
            ii = float(ii) 
            return ii
        elif mode == "int":
            ii = int(ii)
            return ii
        elif mode == "str":
            ii = str(ii)
            return ii
    except (ValueError, TypeError):
        while True:
            try:
                ii = input("[!] Invalid input. Try again.\n> ")
                if mode == "float":
                    ii = float(ii)
                    break
                elif mode == "int":
                    ii = int(ii)
                    break
                elif mode == "str":
                    ii = str(ii)
                    break
            except (ValueError, TypeError):
                pass
        return ii

def show_menu(mm):
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(mm)
