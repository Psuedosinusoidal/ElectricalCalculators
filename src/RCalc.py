# Resistor Calculator Module
# By Pseudosinusoidal
from CalcUtilities import is_valid, show_menu

Band_Colors = "0. Black\n1. Brown\n2. Red\n3. Orange\n4. Yellow\n5. Green\n6. Blue\n7. Violet\n8. Grey\n9. White"
Multipliers = "0. Black\n1. Brown\n2. Red\n3. Orange\n4. Yellow\n5. Green\n6. Blue\n7. Violet\n8. Grey\n9. White\n10. Gold\n11. Silver"
Tolerances = "0. Brown\n1. Red\n2. Green\n3. Blue\n4. Violet\n5. Grey\n6. Gold\n7. Silver"
PPM = "0. Brown\n1. Red\n2. Orange\n3. Yellow\n4. Blue\n5. Violet"

Tolerance_List = {
    "0": "1%",
    "1": "2%",
    "2": "0.5%",
    "3": "0.25%",
    "4": "0.1%",
    "5": "0.05%",
    "6": "5%",
    "7": "10%"
}

PPM_List = {
    "0": "100",
    "1": "50",
    "2": "15",
    "3": "25",
    "4": "10",
    "5": "5"
}

def RCalc():
    formulas = {
        "Voltage": {
            "dividera": lambda Mul, Vo, Load: round(Mul * (Vo / Load), 4),
            "tresistance": lambda Vi, Idiv: Vi / Idiv,
            "R2": lambda Vo, Vi, Rtot: (Vo / Vi) * Rtot,
            "R1": lambda Rtot, R2: Rtot - R2,
            "rdissipation": lambda Idiv, R: round((Idiv ** 2) * R, 4),
            "voltagedrop": lambda Vi, R2, Load, R1: round((Vi * (R2 * Load) / (R2 + Load)) / (R1 + (R2 * Load) / (R2 + Load)), 4),
            "dividerw": lambda Vi, Idiv: round(Vi * Idiv, 4)
        },
        "Current": {
            "placeholder": lambda var: Var + Var
        }
    }
    mm = "[*] Resistor Calculator\n[-1] Exit\n[1] Color Code\n[2] Voltage Division\n[3] Current Division - WIP\n[!] Enter value to proceed.\n"
    show_menu(mm)  # Show the menu at the start
    # Menu Loop
    while True:
        ms = input("> ")

        if ms == "-1":
            print("[!] Terminating module..")
            break

        elif ms == "1": # Color Code
            print("[?] Is this is a 4, 5, or 6 band resistor?")
            while True:
                band_count = input("> ")
                if band_count == "4" or band_count == "5" or band_count == "6":
                    R1 = input(f"{Band_Colors}\n[?] Enter the first color (0-9): ")
                    ii = is_valid(R1, "int")
                    R1 = ii
                    while True:
                        if R1 > 9 or R1 < 0:
                            print("[!] Invalid value, try again.")
                            R1 = input(f"{Band_Colors}\n[?] Enter the first color (0-9): ")
                            ii = is_valid(R1, "int")
                            R1 = ii
                        else:
                            break
                    R2 = input("[?] Enter the second color: ")
                    ii = is_valid(R2, "int")
                    R2 = ii
                    while True:
                        if R2 > 9 or R2 < 0:
                            print("[!] Invalid value, try again.")
                            R2 = input(f"{Band_Colors}\n[?] Enter the second color: ")
                            ii = is_valid(R2, "int")
                            R2 = ii
                        else:
                            break
                    if band_count == "5" or band_count == "6":
                        R5 = input("[?] Enter the third color: ")
                        ii = is_valid(R5, "int")
                        R5 = ii
                        while True:
                            if R5 > 9 or R5 < 0:
                                print("[!] Invalid value, try again.")
                                R5 = input(f"{Band_Colors}\n[?] Enter the third color: ")
                                ii = is_valid(R5, "int")
                                R5 = ii
                            else:
                                break
                        R3 = input(f"{Multipliers}\n[?] Enter the fourth color from the above list (0-11): ")
                        ii = is_valid(R3, "int")
                        R3 = ii
                        while True:
                            if R3 > 11 or R1 < 0:
                                print("[!] Invalid value, try again.")
                                R3 = input(f"{Multipliers}\n[?] Enter the fourth color from the above list (0-11): ")
                                ii = is_valid(R3, "int")
                                R3 = ii
                            else:
                                break
                        R4 = input(f"{Tolerances}\n[?] Enter the fifth color from the above list (0-7): ")
                        ii = is_valid(R4, "int")
                        R4 = ii
                        while True:
                            if R4 > 7 or R4 < 0:
                                print("[!] Invalid value, try again.")
                                R4 = input(f"{Tolerances}\n[?] Enter the fifth color from the above list (0-7): ")
                                ii = is_valid(R4, "int")
                                R4 = ii
                            else:
                                break
                        if band_count == "6":
                            while True:
                                try:
                                    R6 = input(f"{PPM}\n[?] Enter the sixth color from the above list (0-5): ")
                                    ii = is_valid(R6, "int")
                                    R6 = ii
                                    R6 = str(R6)
                                    ppm = PPM_List[R6]
                                    break
                                except KeyError:
                                    print("[!] PPM value is invalid. Please try again.")
                        else:
                            ppm = 0
                            pass
                    else:
                        R3 = input(f"{Multipliers}\n[?] Enter the third color from the above list (0-11): ")
                        ii = is_valid(R3, "int")
                        R3 = ii
                        while True:
                            if R3 > 11 or R3 < 0:
                                print("[!] Invalid value, try again.")
                                R3 = input(f"{Multipliers}\n[?] Enter the third color from the above list (0-11): ")
                                ii = is_valid(R3, "int")
                                R3 = ii
                            else:
                                break
                        R4 = input(f"{Tolerances}\n[?] Enter the fourth color from the above list (0-7): ")
                        ii = is_valid(R4, "int")
                        R4 = ii
                        while True:
                            if R4 > 7 or R4 < 0:
                                print("[!] Invalid value, try again.")
                                R4 = input(f"{Tolerances}\n[?] Enter the fourth color from the above list (0-7): ")
                                ii = is_valid(R4, "int")
                                R4 = ii
                            else:
                                break
                        ppm = 0
                    Mul = "1"
                    if R1 == 0: # If it's black, there is nothing to add. This is num 1.
                        RT = R2
                    elif band_count == "5" or band_count == "6":
                        RT = str(R1) + str(R2) + str(R5)
                    else: # Adds as a string to form base ohms
                        RT = str(R1) + str(R2)
                    if R3 == 0: # If it's black, there is nothing to add. This is a multiplier.
                        RTM = RT
                    else: # If it's going to be affected.
                        if R3 <= 9: # Increasing notation
                            for num in range(R3):
                                Mul = Mul + "0"
                            RTM = int(RT) * int(Mul)
                        elif R3 == 10 or R3 == 11: # Decreasing notation
                            if R3 == 10:
                                RTM = float(RT) * 0.1
                            elif R3 == 11:
                                RTM = float(RT) * 0.01
                        else:
                            print("[!] Fatal error. INVALID MULTIPLIER. Returning to main menu.")
                            show_menu(mm)
                            break
                    R4 = str(R4)
                    try:
                        Tol = Tolerance_List[R4]
                    except KeyError:
                        print("[!] Fatal error. Tolerance value is invalid. Returning to main menu.")
                        show_menu(mm)
                        break
                    RTM = float(RTM)
                    if RTM > 1 and RTM < 999: # Any output between 1-999, not requiring notation.
                        if ppm != 0:
                            null = input(f"[!] Resistor is: {RTM} Ohms, with a tolerance of {Tol} and {ppm} ppm.\n[!] Press enter to proceed..")
                            show_menu(mm)
                            break
                        else:
                            null = input(f"[!] Resistor is: {RTM} Ohms, with a tolerance of {Tol}.\n[!] Press enter to proceed..")
                            show_menu(mm)
                            break
                    else: # Any that require a notation.
                        if RTM >= 0.001 and RTM <= 0.999:
                            Notation = "Mili"
                            if len(str(RTM)) == 3:
                                RT = str(RT) + "00"
                            elif len(str(RTM)) == 4:
                                RT = str(RT) + "0"
                            else:
                                pass
                        elif RTM >= 0.000001 and RTM <= 0.000999:
                            Notation = "Micro"
                        elif RTM >= 1000 and RTM <= 999999:
                            Notation = "Kilo"
                        elif RTM >= 1000000 and RTM <= 999999999:
                            Notation = "Mega"
                        elif RTM >= 1000000000 and RTM <= 999999999999:
                            Notation = "Giga"
                        else:
                            Notation = "ERROR"
                        if ppm != 0:
                            null = input(f"[!] Resistor is: {RTM} Ohms, or {RT} {Notation}Ohms. With a tolerance of {Tol} and {ppm} ppm.\n[!] Press enter to proceed..")
                            show_menu(mm)
                            break
                        else:
                            null = input(f"[!] Resistor is: {RTM} Ohms, or {RT} {Notation}Ohms. With a tolerance of {Tol}.\n[!] Press enter to proceed..")
                            show_menu(mm)
                            break
                else:
                    print("[!] Invalid value, try again.")
        
        elif ms == "2": # Voltage Division
            Vi = input("\n[?] Enter input voltage: ")
            ii = is_valid(Vi, "float")
            Vi = ii
            Vo = input("[?] Enter desired output voltage: ")
            ii = is_valid(Vo, "float")
            Vo = ii
            Load = input("[?] Enter LOAD resistance (Ohms): ")
            ii = is_valid(Load, "float")
            Load = ii
            Mul = input("[!] Lower multiplier means LESS resistance and MORE current in division circuit (Typically 10)\n[?] Enter multiplier: ")
            ii = is_valid(Mul, "float")
            Mul = ii
            while True:
                Idiv = formulas["Voltage"]["dividera"](Mul=Mul, Vo=Vo, Load=Load)
                Rtot = formulas["Voltage"]["tresistance"](Vi=Vi, Idiv=Idiv)
                R2 = formulas["Voltage"]["R2"](Vo=Vo, Vi=Vi, Rtot=Rtot)
                R = R2 
                PR2 = formulas["Voltage"]["rdissipation"](Idiv=Idiv, R=R)
                R1 = formulas["Voltage"]["R1"](Rtot=Rtot, R2=R2)
                R = R1
                PR1 = formulas["Voltage"]["rdissipation"](Idiv=Idiv, R=R)
                Vo_Chk = formulas["Voltage"]["voltagedrop"](Vi=Vi, R2=R2, Load=Load, R1=R1)
                Pdiv = formulas["Voltage"]["dividerw"](Vi=Vi, Idiv=Idiv)
                Idiv = round(Idiv, 4)
                R1 = round(R1, 4)
                R2 = round(R2, 4)
                print(f"\n\n[*] Divider total amperage: {Idiv}A\n[*] Divider total wattage: {Pdiv}W\n[*] Resistor 1: {R1} Ohms, {PR1}W\n[*] Resistor 2: {R2} Ohms, {PR2}W\n[*] Voltage with load: {Vo_Chk}V")
                vdm  = input("\n[!] Type 'mul' to try a different divider resistance, 'volt' to change the voltages, or 'load' to change load resistance. Otherwise, press enter to return to main menu.\n> ")
                if vdm == "mul":
                    Mul = input("[?] Enter new multiplier: ")
                    ii = is_valid(Mul, "float")
                    Mul = ii
                elif vdm == "volt":
                    Vi = input("\n[?] Enter input voltage: ")
                    ii = is_valid(Vi, "float")
                    Vi = ii
                    Vo = input("[?] Enter desired output voltage: ")
                    ii = is_valid(Vo, "float")
                    Vo = ii
                elif vdm == "load":
                    Load = input("[?] Enter LOAD resistance (Ohms): ")
                    ii = is_valid(Load, "float")
                    Load = ii
                else:
                    show_menu(mm)
                    break
            
        elif ms == "3": # Current Division
            pass
        
        else:
            print("[!] Invalid value, try again.")
            pass
