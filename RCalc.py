# Resistor Calculator Module
# By Pseudosinusoidal
from time import sleep
from CalcUtilities import is_valid

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
    # Menu Variables
    buffer = "\n" * 100
    ms = 0 # Menu Select
    mm = "[*] Resistor Calculator\n[1] Color Code\n[2] Voltage Division\n[3] Current Division - WIP\n[-1] Exit\n[!] Enter value to proceed.\n"
    print(buffer + mm)
    # Menu Loop
    while ms != "-1":
        ms = input("> ")
        if ms == "-1":
            print("[!] Terminating module.")
            break
        elif ms == "1": # Color Code
            print("[?] Is this is a 4, 5, or 6 band resistor?")
            while True:
                band_count = input("> ")
                if band_count == "4" or band_count == "5" or band_count == "6":
                    R1 = input(f"{Band_Colors}\n[?] Enter the first color (0-9): ")
                    ii = is_valid(R1, "int")
                    R1 = ii
                    R2 = input("[?] Enter the second color: ")
                    ii = is_valid(R2, "int")
                    R2 = ii
                    if band_count == "5" or band_count == "6":
                        R5 = input("[?] Enter the third color: ")
                        ii = is_valid(R5, "int")
                        R5 = ii
                        R3 = input(f"{Multipliers}\n[?] Enter the fourth color from the above list (0-11): ")
                        ii = is_valid(R3, "int")
                        R3 = ii
                        R4 = input(f"{Tolerances}\n[?] Enter the fifth color from the above list (0-7): ")
                        ii = is_valid(R4, "int")
                        R4 = ii
                        if band_count == "6":
                            R6 = input(f"{PPM}\n[?] Enter the sixth color from the above list (0-5): ")
                            ii = is_valid(R6, "int")
                            R6 = ii
                            R6 = str(R6)
                            try:
                                ppm = PPM_List[R6]
                            except KeyError:
                                print("[!] PPM value is invalid. Returning to main menu.")
                                sleep(2)
                                break
                        else:
                            ppm = 0
                            pass
                    else:
                        R3 = input(f"{Multipliers}\n[?] Enter the third color from the above list (0-11): ")
                        ii = is_valid(R3, "int")
                        R3 = ii
                        R4 = input(f"{Tolerances}\n[?] Enter the fourth color from the above list (0-7): ")
                        ii = is_valid(R4, "int")
                        R4 = ii
                        ppm = 0
                    Mul = "1"
                    if R1 == 0: # If it's black, there is nothing to add. This is num 1.
                        RT = R2
                    elif band_count == "5" or band_count == "6":
                        RT = str(R1) + str(R2) + str(R5)
                    else: # Adds as a string to form base ohms
                        RT = str(R1) + str(R2)
                    if R3 == 0: # If it's black, there is nothing to add. This is multiplier.
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
                            print("[!] Multiplier value is invalid. Returning to main menu.")
                            sleep(2)
                            break
                    R4 = str(R4)
                    try:
                        Tol = Tolerance_List[R4]
                    except KeyError:
                        print("[!] Tolerance value is invalid. Returning to main menu.")
                        sleep(2)
                        break
                    RTM = float(RTM)
                    if RTM > 1 and RTM < 999: # Any output between 1-999, not requiring notation.
                        if ppm != 0:
                            null = input(f"[!] Resistor is: {RTM} Ohms, with a tolerance of {Tol} and {ppm} ppm.\n[!] Press enter to proceed..")
                            sleep(1.5)
                            print(buffer + mm)
                            break
                        else:
                            null = input(f"[!] Resistor is: {RTM} Ohms, with a tolerance of {Tol}.\n[!] Press enter to proceed..")
                            sleep(1.5)
                            print(buffer + mm)
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
                            sleep(1.5)
                            print(buffer + mm)
                            break
                        else:
                            null = input(f"[!] Resistor is: {RTM} Ohms, or {RT} {Notation}Ohms. With a tolerance of {Tol}.\n[!] Press enter to proceed..")
                            sleep(1.5)
                            print(buffer + mm)
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
                LoadI = Vo / Load # Finding amperage of load
                Idiv = Mul * LoadI # Finding amperage of divider
                Rtot = Vi / Idiv # Finding total required resistance
                Vr = Vo / Vi # Finding voltage ratio
                R2 = Vr * Rtot # Finding resistor 2's value
                R1 = Rtot - R2 # Finding resistor 1's value
                R2_Chk = (R2 * Load) / (R2 + Load) # Checking load impedance / Voltage drop
                Vo_Chk = (Vi * R2_Chk) / (R1 + R2_Chk) # Finding post drop voltage
                Pdiv = Vi * Idiv # Finding total wattage of divider
                PR1 = (Idiv ** 2) * R1 # Finding power dissipation of R1
                PR2 = (Idiv ** 2) * R2 # Finding power dissipation of R2
                Idiv = round(Idiv, 4)
                Pdiv = round(Pdiv, 4)
                R1 = round(R1, 4)
                R2 = round(R2, 4)
                PR1 = round(PR1, 4)
                PR2 = round(PR2, 4)
                Vo_Chk = round(Vo_Chk, 4)
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
                    sleep(1.5)
                    print(buffer + mm)
                    break
            
        elif ms == "3": # Current Division
            pass
        
        else:
            print("[!] Invalid value, try again.")
            pass
