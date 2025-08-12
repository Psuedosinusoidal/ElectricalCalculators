'''
    Title: CircuitSolver GUI
    Version: 0.1.0

    Calculations By: PseudoSinusoidal
    Developed By: Floppy

    Started: 2025-08-10
    Updated: 2025-08-11
'''

# ========== Setup ========== #
# Imports
import tkinter as tk
from tkinter import PhotoImage

# Tkinter setup
root = tk.Tk()
root.geometry('400x350')
root.title('CircuitSolver GUI - Version: 0.1.0')
# root.iconbitmap(r'../res/circuit_solver_gui_icon.ico')


# ========== Functions ========== #
def nothing():
    print("nothing")

def fun_frm_enable_555_timer():
    gui_frm_555_timer.place(x=0, y=0)
    print("enabled 555 timer")

def fun_btn_555_timer_solve():
    # Try to convert entries into floats, if failed output error.
    try:
        var_555_timer_frequency = float(gui_ent_555_timer_frequency.get())
        var_555_timer_c1 = float(gui_ent_555_timer_c1.get())

    except ValueError:
        print("> [!] Could not convert to variables!")
        return

    # If converted print the output.
    print(var_555_timer_frequency)
    print(var_555_timer_c1)

    # Do the calculations.
    IsoZ = 1.44 / var_555_timer_frequency  # Isolating the combined Capacitance and Resistance from the Frequency.
    IsoY = IsoZ / var_555_timer_c1  # Isolating Capacitance from the Resistance to find Total Resistance
    ReqOhmsPer = IsoY / 3  # Finding Required Ohms per the 2 resistors that would equal a balanced high and low time. R1 is equal to 1 of itself, whereas R2 is equal to 2 of itself.
    ReqOhmsPer = round(ReqOhmsPer, 1)
    # Finding High duration
    time_high = 0.693 * (ReqOhmsPer * 2) * var_555_timer_c1
    # Finding Low duration
    time_low = 0.693 * ReqOhmsPer * var_555_timer_c1

    # Output the results to the GUI entries.
    gui_stat_555_timer_r1.config(text=ReqOhmsPer)
    gui_stat_555_timer_r2.config(text=ReqOhmsPer)
    gui_stat_555_timer_time_high.config(text=time_high)
    gui_stat_555_timer_time_low.config(text=time_low)


# ========== GUI ========== #
# ===== Menubar ===== #
gui_menubar = tk.Menu()

# File menu
gui_file_menu = tk.Menu(gui_menubar, tearoff=False)  # Create file menu
gui_menubar.add_cascade(menu=gui_file_menu, label="File")  # Add a cascade
gui_file_menu.add_command(label="New", command=nothing)  # Add a command
gui_file_menu.add_separator()  # Add a separator
gui_file_menu.add_command(label="Exit", command=root.destroy)


# Calculator menu
gui_calculator_menu = tk.Menu(gui_menubar, tearoff=False)
gui_menubar.add_cascade(menu=gui_calculator_menu, label="Calculators")
gui_calculator_menu.add_command(label="555 Timer", command=fun_frm_enable_555_timer)
gui_calculator_menu.add_command(label="Resistor Values", command=nothing)
gui_calculator_menu.add_command(label="Ohm's Law", command=nothing)

# ===== Frames ===== #
# ===== 555 timer
gui_frm_555_timer = tk.Frame(root, width=400, height=350)

# 555 timer title
gui_lbl_555_timer_title = tk.Label(gui_frm_555_timer, text="555 Timer Calculator", relief='groove')
gui_lbl_555_timer_title.place(x=0, y=0, width=400, height=20)

# 555 timer frequency and capacitor inputs
gui_lbl_555_timer_frequency = tk.Label(gui_frm_555_timer, text="Frequency(Hz):", relief='groove')
gui_lbl_555_timer_frequency.place(x=0, y=21, width=105, height=20)
gui_ent_555_timer_frequency = tk.Entry(gui_frm_555_timer)
gui_ent_555_timer_frequency.place(x=105, y=21, width=65, height=20)

gui_lbl_555_timer_c1 = tk.Label(gui_frm_555_timer, text="Capacitor(F):", relief='groove')
gui_lbl_555_timer_c1.place(x=175, y=21, width=95, height=20)
gui_ent_555_timer_c1 = tk.Entry(gui_frm_555_timer)
gui_ent_555_timer_c1.place(x=270, y=21, width=65, height=20)

# 555 timer solve button
gui_btn_555_timer_solve = tk.Button(gui_frm_555_timer, text="Solve", state='normal', relief='raised', command=fun_btn_555_timer_solve)
gui_btn_555_timer_solve.place(x=0, y=42, width=45, height=20)

# Resistor 1 and resistor 2 outputs
gui_lbl_555_timer_r1 = tk.Label(gui_frm_555_timer, text="Resistor 1(Ω):", relief='groove')
gui_lbl_555_timer_r1.place(x=0, y=63, width=95, height=20)
gui_stat_555_timer_r1 = tk.Label(gui_frm_555_timer, relief='sunken')
gui_stat_555_timer_r1.place(x=95, y=63, width=75, height=20)

gui_lbl_555_timer_r2 = tk.Label(gui_frm_555_timer, text="Resistor 2(Ω):", relief='groove')
gui_lbl_555_timer_r2.place(x=175, y=63, width=95, height=20)
gui_stat_555_timer_r2 = tk.Label(gui_frm_555_timer, relief='sunken')
gui_stat_555_timer_r2.place(x=270, y=63, width=75, height=20)

# Time high and time low outputs
gui_lbl_555_timer_time_high = tk.Label(gui_frm_555_timer, text="Time High(S):", relief='groove')
gui_lbl_555_timer_time_high.place(x=0, y=84, width=95, height=20)
gui_stat_555_timer_time_high = tk.Label(gui_frm_555_timer, relief='sunken')
gui_stat_555_timer_time_high.place(x=95, y=84, width=75, height=20)

gui_lbl_555_timer_time_low = tk.Label(gui_frm_555_timer, text="Time Low(S):", relief='groove')
gui_lbl_555_timer_time_low.place(x=175, y=84, width=95, height=20)
gui_stat_555_timer_time_low = tk.Label(gui_frm_555_timer, relief='sunken')
gui_stat_555_timer_time_low.place(x=270, y=84, width=75, height=20)

# Add 555 timer example
gui_img_555_timer_example = tk.PhotoImage(file='../res/555_timer_example.png')
gui_lbl_555_timer_example = tk.Label(gui_frm_555_timer, image=gui_img_555_timer_example)
gui_lbl_555_timer_example.place(x=5, y=109)


# Loops... Loops...
root.config(menu=gui_menubar)
root.mainloop()
