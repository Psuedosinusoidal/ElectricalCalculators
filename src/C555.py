# 555 Timer Calculator Module
# By Pseudosinusoidal
from CalcUtilities import is_valid, show_menu

def Calc555():
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
                    IsoX = Dur / 1.1
                    if C1 == 0.00022:
                        R1 = IsoX / C1
                        R1 = round(R1, 4)
                        null = input(f"[!] The required resistance to achieve {Dur} seconds with {C1} Farads is: {R1}~ Ohms.\n[!] Press enter to continue.")
                    else:
                        R1 = IsoX / C1
                        R1 = round(R1, 4)
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
                    Time = 1.1 * R1 * C1
                    Time = round(Time, 4)
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
                    IsoZ = 1.44 / Hz # Isolating the combined Capacitance and Resistance from the Frequency.
                    IsoY = IsoZ / C1 # Isolating Capacitance from the Resistance to find Total Resistance
                    ReqOhmsPer = IsoY / 3 # Finding Required Ohms per the 2 resistors that would equal a balanced high and low time. R1 is equal to 1 of itself, whereas R2 is equal to 2 of itself.
                    ReqOhmsPer = round(ReqOhmsPer, 1)
                    # Finding High duration
                    Th = 0.693 * (ReqOhmsPer * 2) * C1
                    Th = round(Th, 5)
                    # Finding Low duration
                    Tl = 0.693 * ReqOhmsPer * C1
                    Tl = round(Tl, 5)
                    DC = Th / (Th + Tl) * 100
                    DC = round(DC, 5)
                    null = input(f"[!] To achieve {Hz} Hz at {C1} Farads, R1 and R2 must be {ReqOhmsPer} Ohms each or a Total Resistance of {IsoY} Ohms when R2 is multiplied by 2, and added with R1. If either R1 or R2 is under 1k Ohms, it may damage the 555. C1 will need adjusted.\n[!] Time High: {Th}s\n[!] Time Low: {Tl}s\n[!] Duty Cycle: {DC}%\n[!] To change Resistance values and therefore Time High and Time Low, type 'editr' instead of blank.\n[!] Press enter to continue.\n> ")
                    if null == "editr":
                        IsoK = IsoY / 2
                        IsoK -= 1
                        print(f"\nThe total required value is {IsoY} Ohms which was by default achieved by {ReqOhmsPer} Ohms per resistor.\nThe closer R2 is to the total required value when multiplied by 2, and the closer R1 is to 0 Ohms, the more equal their time will be. Time low cannot be higher than time high.\n[!] Type 'exit' to quit\n")
                        while True:
                            R2 = input(f"[?] Enter new R2 value [min: 1, max: {IsoK}]: ")
                            if R2 == "exit":
                                break
                            else:
                                ii = is_valid(R2, "float")  # Validating Data Input
                                R2 = ii
                                if R2 > IsoK or R2 < 1:
                                    print("[!] Out of range")
                                else:
                                    R1 = R2 * 2 # Finding R1
                                    R1 = IsoY - R1
                                    # Finding High duration
                                    Th = 0.693 * (R1 + R2) * C1
                                    Th = round(Th, 5)
                                    # Finding Low duration
                                    Tl = 0.693 * R2 * C1
                                    Tl = round(Tl, 5)
                                    DC = Th / (Th + Tl) * 100
                                    DC = round(DC, 5)
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
                    R2 = R2 * 2
                    RT = R1 + R2
                    Denominator = RT * C1
                    Hz = 1.44 / Denominator
                    # Finding High duration
                    Th = 0.693 * (R1 + R2) * C1
                    Th = round(Th, 5)
                    # Finding Low duration
                    Tl = 0.693 * R2 * C1
                    Tl = round(Tl, 5)
                    DC = Th / (Th + Tl) * 100
                    DC = round(DC, 5)
                    null = input(f"Using a total resistance of {RT} Ohms and a capacitance of {C1} Farads, you will achieve {Hz} Hz with a duty cycle of {DC}%.\n[!] Press enter to continue.")
                    show_menu(mm)
                    break

                else:
                    print("[!] Invalid value. Try again.")

        else:
            print("[!] Invalid value. Try again.")
            pass
