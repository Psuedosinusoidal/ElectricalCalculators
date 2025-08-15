# 555 Timer Calculator Module
# By Pseudosinusoidal
from CalcUtilities import is_valid, show_menu

def Calc555():
    formulas = {
        "Monostable": {
            "duration": lambda Dur, C1: round((Dur / 1.1) / C1, 4), # Find R1 from Duration and C1
            "components": lambda R1, C1: round(1.1 * R1 * C1, 4) # Find Duration from R1 and C1
        },
        "Astable": {
            "frequency": lambda Hz, C1: round((1.44 / Hz) / C1, 5), # Find total resistance from Hz and C1
            "ohmsper": lambda TotR: round(TotR / 3, 2), # Find R1 and R2 from Total Resistance
            "components": lambda R1, R2, C1: round(1.44 / (((R2 * 2) + R1) * C1), 5), # Find Hz from R1, R2, and C1.
            "highdur": lambda TotR, C1: round(0.693 * ((TotR / 3) * 2) * C1, 5), # Find High Time from Total Resistance and C1.
            "lowdur": lambda TotR, C1: round(0.693 * (TotR / 3) * C1, 5), # Find Low Time from Total Resistance and C1.
            "duty": lambda Th, Tl: round(Th / (Th + Tl) * 100, 5) # Find Duty Cycle from Time High and Time Low.
        }
    }
    mm = "[*] 555 Timer Calculator\n[-1] Exit\n[1] Monostable \n[2] Astable\n[!] Enter value to proceed.\n"
    show_menu(mm)  # Show the menu at the start
    # Menu Loop
    while True:
        ms = input("> ")
        
        if ms == "-1": # Exit
            print("[!] Terminating module..")
            break

        # Monostable
        elif ms == "1":
            print("[*] Monostable Formula T = 1.1 * R1 * C1\n Find by:\n[1] Duration Required\n[2] Component Values")
            while True:
                mono_menu = input("> ")
                if mono_menu == "1": # Finding Monostable Components from Required Duration
                    Dur = input("[?] Enter Duration in Seconds: ")
                    ii = is_valid(Dur, "float")
                    Dur = ii
                    C1 = input("[?] Default capacitor is 220uF. Press enter to continue, or enter a value in Farads.\n> ")
                    if C1 == "":
                        C1 = float(0.00022)
                    else:
                        ii = is_valid(C1, "float")
                        C1 = ii
                        print(f"[!] Going with {C1} Farads")
                    R1 = formulas["Monostable"]["duration"](Dur=Dur, C1=C1)
                    null = input(f"[!] The required resistance to achieve {Dur} seconds with {C1} Farads is: {R1}~ Ohms.\n[!] Press enter to continue.")
                    show_menu(mm)
                    break

                elif mono_menu == "2": # Finding Monostable Timing from Input Components
                    R1 = input("[?] Resistor 1 Value in Ohms: ")
                    ii = is_valid(R1, "float")
                    R1 = ii
                    C1 = input("[?] Capacitor 1 Value in Farads: ")
                    ii = is_valid(C1, "float")
                    C1 = ii
                    Time = formulas["Monostable"]["components"](R1=R1, C1=C1)
                    null = input(f"[!] These components would produce a duration of: {Time}s\n[!] Press enter to continue.")
                    show_menu(mm)
                    break
                else:
                    print("[!] Invalid value. Try again.")
            
        # Astable
        elif ms == "2":
            print("[*] Astable Mode\n Find by:\n[1] Frequency Required\n[2] Component Values")
            while True:
                asta_menu = input("> ")
                if asta_menu == "1": # Finding Astable Components from Required Frequency
                    print("[*] Astable Formula Hz = 1.44 / (R1 + 2*R2) * C1\n")
                    Hz = input("[?] Enter the desired frequency in Hertz.\n> ")
                    ii = is_valid(Hz, "float")
                    Hz = ii
                    C1 = input("[?] Enter a preferred capacitance value. 10nF recommended for frequencies over 1Khz, 1uF for under.\n> ")
                    ii = is_valid(C1, "float")
                    C1 = ii
                    TotR = formulas["Astable"]["frequency"](Hz=Hz, C1=C1)
                    ReqOhmsPer = formulas["Astable"]["ohmsper"](TotR=TotR)
                    Th = formulas["Astable"]["highdur"](TotR=TotR, C1=C1)
                    Tl = formulas["Astable"]["lowdur"](TotR=TotR, C1=C1)
                    DC = formulas["Astable"]["duty"](Th=Th, Tl=Tl)
                    null = input(f"[!] To achieve {Hz} Hz at {C1} Farads, R1 and R2 must be {ReqOhmsPer} Ohms each or a Total Resistance of {TotR} Ohms when R2 is multiplied by 2, and added with R1. If either R1 or R2 is under 1k Ohms, it may damage the 555. C1 will need adjusted.\n[!] Time High: {Th}s\n[!] Time Low: {Tl}s\n[!] Duty Cycle: {DC}%\n[!] To change Resistance values and therefore Time High and Time Low, type 'editr' instead of blank.\n[!] Press enter to continue.\n> ")
                    if null == "editr":
                        MaxR2 = (TotR / 2) - 1 # Finds and caps R2 value
                        print(f"\nThe total required value is {TotR} Ohms which was by default achieved by {ReqOhmsPer} Ohms per resistor.\nThe closer R2 is to the total required value when multiplied by 2, and the closer R1 is to 0 Ohms, the more equal their time will be. Time low cannot be higher than time high.\n[!] Type 'exit' to quit\n")
                        while True:
                            R2 = input(f"[?] Enter new R2 value [min: 1, max: {MaxR2}]: ")
                            if R2 == "exit":
                                break
                            else:
                                ii = is_valid(R2, "float")  # Validating Data Input
                                R2 = ii
                                if R2 > MaxR2 or R2 < 1:
                                    print("[!] Out of range")
                                else:
                                    R1 = TotR - (R2 * 2) # Finding R1
                                    Th = round(0.693 * (R1 + R2) * C1, 5) # Finding High duration
                                    Tl = round(0.693 * R2 * C1, 5) # Finding Low duration
                                    DC = formulas["Astable"]["duty"](Th=Th, Tl=Tl)
                                    print(f"[R1] {R1} Ohms\n[R2] {R2} Ohms\n[!] Time High: {Th}s\n[!] Time Low: {Tl}s\n[!] Duty Cycle: {DC}%\n")
                        show_menu(mm)
                        break
                    else:
                        show_menu(mm)
                        break

                elif asta_menu == "2": # Finding Astable Timing from Input Components
                    R1 = input("[?] Resistor 1 Value in Ohms: ")
                    ii = is_valid(R1, "float")
                    R1 = ii
                    R2 = input("[?] Resistor 2 Value in Ohms: ")
                    ii = is_valid(R2, "float")
                    R2 = ii
                    C1 = input("[?] Capacitor Value in Farads: ")
                    ii = is_valid(C1, "float")
                    C1 = ii
                    Hz = formulas["Astable"]["components"](R1=R1, R2=R2, C1=C1)
                    Th = round(0.693 * (R1 + R2) * C1, 5) # Finding High duration
                    Tl = round(0.693 * R2 * C1, 5) # Finding Low duration
                    DC = formulas["Astable"]["duty"](Th=Th, Tl=Tl)
                    null = input(f"Using R1 {R1} Ohms, R2 {R2} Ohms and a capacitance of {C1} Farads, you will achieve {Hz} Hz.\n[!] Time High: {Th}s\n[!] Time Low: {Tl}s\n[!] Duty Cycle: {DC}%\n[!] Press enter to continue.")
                    show_menu(mm)
                    break

                else:
                    print("[!] Invalid value. Try again.")

        else:
            print("[!] Invalid value. Try again.")
            pass
