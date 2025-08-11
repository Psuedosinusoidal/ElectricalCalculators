''' 
    Title: CircuitSolver CMD
    Version: 0.1.1

    Made By: PseudoSinusoidal

    Started: 2025-08-09
    Updated: 2025-08-11
'''
from time import sleep
from C555 import Calc555 # 555 IC Timer Calculator
from OLaw import OLawBase # Ohm's Law Calculator
from RCalc import RCalc # Resistor Tools
import os

# Module Dictionary
modules = {
    "1": Calc555,
    "2": OLawBase,
    "3": RCalc
}

mm = "[*] Electrical Calculators by Pseudosinusoidal\n[!] Enter the corresponding number to use module.\n[-1] Exit\n[1] 555 Timer IC\n[2] Ohm's Law\n[3] Resistor Calculator"
def show_menu():
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(mm)

print(mm)
while True:
    ms = input("> ")
    if ms == "-1":
        print("[!] Terminating program..")
        exit()
    elif ms in modules: # Find module number
        modules[ms]()
        show_menu()  # Show the menu again after module execution
    else:
        print("[!] Invalid value.")
