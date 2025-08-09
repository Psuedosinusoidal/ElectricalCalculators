# Electrical Calculator Base
# By Pseudosinusoidal
from time import sleep
from C555 import Calc555 # 555 IC Timer Calculator
from OLaw import OLawBase # Ohm's Law Calculator
from RCalc import RCalc # Resistor Tools

buffer = "\n" * 100 # Used instead of os.system(clear) due to terminal compat
ms = 0 # Menu Select
mm = "[*] Electrical Calculators by Pseudosinusoidal\n[!] Enter the corresponding number to use module.\n[-1] Exit\n[1] 555 Timer IC\n[2] Ohm's Law\n[3] Resistor Calculator\n(Everything from this point is WIP.)\n[4] Capacitor Calculator\n[5] Inductors Calculator\n[6] Reactance and Impedance\n[7] Frequency\n[8] Amperage to AWG and Wire Type & Voltage Drop over Distance\n[9] RMS\n[10] Battery\n[11] Gear Ratio / RPM / PWM Calculator\n[12] Power Factor\n[13] Transformers\n[14] 3-Phase\n[15] Transistors"
print(mm)
sleep(2)
while ms != "-1": # Exit
    ms = input("> ")
    if ms == "-1":
        print("[!] Terminating program..")
        exit()
    elif ms == "1": # 555 IC Timer
        Calc555()
        print(buffer + mm)
    elif ms == "2": # Ohm's Law Calculator
        OLawBase()
        print(buffer + mm)
    elif ms == "3": # Resistor Calculator
        RCalc()
        print(buffer + mm)
    else:
        print("[!] Invalid value.")