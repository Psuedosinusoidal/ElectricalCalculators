# Ohm's Law Calculator Module
# By Pseudosinusoidal
import math
from CalcUtilities import is_valid, show_menu

def OLawBase():
    mm = "[*] Ohm's Law Calculator\n[-1] Exit \n[1] Formula Sheet\n[2] Find Power\n[3] Find Voltage\n[4] Find Current\n[5] Find Resistance\n[!] Enter value to proceed.\n"
    show_menu(mm)
    # Menu Loop
    while True:
        ms = input("> ")
        
        # Exit
        if ms == "-1":
            print("[!] Terminating module..")
            break
    
        # Formulas
        elif ms == "1":
            print("[!] Ohm's Law Formulas:\n[Power] V * I\n[Power] R * I^2\n[Power] V^2 / R\n[Voltage] R * I\n[Voltage] P / I\n[Voltage] √P * R\n[Current] √P / R\n[Current] P / V\n[Current] V / R\n[Resistance] V / I\n[Resistance] V^2 / P\n[Resistance] P / I^2\n")
        
        # Power
        elif ms == "2":
            while True:
                formula_s = input("[?] Select Formula\n[1] V * I\n[2] R * I^2\n[3] V^2 / R\n> ")
                if formula_s == "1":
                    V = input("[?] Enter Voltage: ")
                    ii = is_valid(V, "float")
                    V = ii
                    I = input("[?] Enter Amperage: ")
                    ii = is_valid(I, "float")
                    I = ii
                    P = V * I
                    null = input(f"[!] {P} Watts. Press enter to continue..\n\n")
                    show_menu(mm)
                    break
                elif formula_s == "2":
                    R = input("[?] Enter Resistance: ")
                    ii = is_valid(R, "float")
                    R = ii
                    I = input("[?] Enter Amperage: ")
                    ii = is_valid(I, "float")
                    I = ii
                    P = R * I^2
                    null = input(f"[!] {P} Watts. Press enter to continue..\n\n")
                    show_menu(mm)
                    break
                elif formula_s == "3":
                    V = input("[?] Enter Voltage: ")
                    ii = is_valid(V, "float")
                    V = ii
                    R = input("[?] Enter Resistance: ")
                    ii = is_valid(R, "float")
                    R = ii
                    P = V^2 / R
                    null = input(f"[!] {P} Watts. Press enter to continue..\n\n")
                    show_menu(mm)
                    break
                else:
                    print("[!] Invalid value, please try again.")
        
        # Voltage
        elif ms == "3":
            while True:
                formula_s = input("[?] Select Formula\n[1] R * I\n[2] P / I\n[3] √P * R\n> ")
                if formula_s == "1":
                    R = input("[?] Enter Resistance: ")
                    ii = is_valid(R, "float")
                    R = ii
                    I = input("[?] Enter Amperage: ")
                    ii = is_valid(I, "float")
                    I = ii
                    V = R * I
                    null = input(f"[!] {V} Volts. Press enter to continue..\n\n")
                    show_menu(mm)
                    break
                elif formula_s == "2":
                    P = input("[?] Enter Wattage: ")
                    ii = is_valid(P, "float")
                    P = ii
                    I = input("[?] Enter Amperage: ")
                    ii = is_valid(I, "float")
                    I = ii
                    V = P / I
                    null = input(f"[!] {V} Volts. Press enter to continue..\n\n")
                    show_menu(mm)
                    break
                elif formula_s == "3":
                    P = input("[?] Enter Wattage: ")
                    ii = is_valid(P, "float")
                    P = ii
                    R = input("[?] Enter Resistance: ")
                    ii = is_valid(R, "float")
                    R = ii
                    V = math.sqrt(P) * R
                    null = input(f"[!] {V} Volts. Press enter to continue..\n\n")
                    show_menu(mm)
                    break
                else:
                    print("[!] Invalid value, please try again.")
        
        # Current
        elif ms == "4":
            while True:
                formula_s = input("[?] Select Formula\n[1] √P / R\n[2] P / V\n[3] V / R\n> ")
                if formula_s == "1":
                    P = input("[?] Enter Wattage: ")
                    ii = is_valid(P, "float")
                    P = ii
                    R = input("[?] Enter Resistance: ")
                    ii = is_valid(R, "float")
                    R = ii
                    I = math.sqrt(P) / R
                    null = input(f"[!] {I} Amps. Press enter to continue..\n\n")
                    show_menu(mm)
                    break
                elif formula_s == "2":
                    P = input("[?] Enter Wattage: ")
                    ii = is_valid(P, "float")
                    P = ii
                    V = input("[?] Enter Voltage: ")
                    ii = is_valid(V, "float")
                    V = ii
                    I = P / V
                    null = input(f"[!] {I} Amps. Press enter to continue..\n\n")
                    show_menu(mm)
                    break
                elif formula_s == "3":
                    V = input("[?] Enter Voltage: ")
                    ii = is_valid(V, "float")
                    V = ii
                    R = input("[?] Enter Resistance: ")
                    ii = is_valid(R, "float")
                    R = ii
                    I = V / R
                    null = input(f"[!] {I} Amps. Press enter to continue..\n\n")
                    show_menu(mm)
                    break
                else:
                    print("[!] Invalid value, please try again.")
        
        # Resistance
        elif ms == "5":
            while True:
                formula_s = input("[?] Select Formula\n[1] V / I\n[2] V^2 / P\n[3] P / I^2\n> ")
                if formula_s == "1":
                    V = input("[?] Enter Voltage: ")
                    ii = is_valid(V, "float")
                    V = ii
                    I = input("[?] Enter Amperage: ")
                    ii = is_valid(I, "float")
                    I = ii
                    R = V / I
                    null = input(f"[!] {R} Ohms. Press enter to continue..\n\n")
                    show_menu(mm)
                    break
                elif formula_s == "2":
                    V = input("[?] Enter Voltage: ")
                    ii = is_valid(V, "float")
                    V = ii
                    P = input("[?] Enter Wattage: ")
                    ii = is_valid(P, "float")
                    P = ii
                    R = V^2 / P
                    null = input(f"[!] {R} Ohms. Press enter to continue..\n\n")
                    show_menu(mm)
                    break
                elif formula_s == "3":
                    P = input("[?] Enter Wattage: ")
                    ii = is_valid(P, "float")
                    P = ii
                    I = input("[?] Enter Amperage: ")
                    ii = is_valid(I, "float")
                    I = ii
                    R = P / I^2
                    null = input(f"[!] {R} Ohms. Press enter to continue..\n\n")
                    show_menu(mm)
                    break
                else:
                    print("[!] Invalid value, please try again.")
        else:
            print("[!] Invalid value, please try again.")
