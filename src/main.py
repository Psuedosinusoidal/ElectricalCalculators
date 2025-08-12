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
        var_555_timer_capacitor = float(gui_ent_555_timer_capacitor.get())

    except ValueError:
        print("> [!] Could not convert to variables!")
        return

    # If converted print the output.
    print(var_555_timer_frequency)
    print(var_555_timer_capacitor)

    # Do the conversions



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
# 555 timer frame (NOTE: Put into library later on!)
gui_frm_555_timer = tk.Frame(root, width=400, height=350)

# 555 timer title
gui_lbl_555_timer_title = tk.Label(gui_frm_555_timer, text="555 Timer Calculator", relief='groove')
gui_lbl_555_timer_title.place(x=0, y=0, width=400, height=20)

# 555 timer frequency and capacitor inputs
gui_lbl_555_timer_frequency = tk.Label(gui_frm_555_timer, text="Frequency(Hz):", relief='groove')
gui_lbl_555_timer_frequency.place(x=0, y=21, width=105, height=20)
gui_ent_555_timer_frequency = tk.Entry(gui_frm_555_timer)
gui_ent_555_timer_frequency.place(x=105, y=21, width=65, height=20)

gui_lbl_555_timer_capacitor = tk.Label(gui_frm_555_timer, text="Capacitor(Fx):", relief='groove')
gui_lbl_555_timer_capacitor.place(x=175, y=21, width=95, height=20)
gui_ent_555_timer_capacitor = tk.Entry(gui_frm_555_timer)
gui_ent_555_timer_capacitor.place(x=270, y=21, width=65, height=20)

# 555 timer solve button
gui_btn_555_timer_solve = tk.Button(gui_frm_555_timer, text="Solve", state='normal', relief='raised', command=fun_btn_555_timer_solve)
gui_btn_555_timer_solve.place(x=0, y=42, width=45, height=20)

# Resistor 1 and resistor 2 outputs
gui_lbl_555_timer_resistor_1 = tk.Label(gui_frm_555_timer, text="Resistor 1(Ω):", relief='groove')
gui_lbl_555_timer_resistor_1.place(x=0, y=63, width=95, height=20)
gui_stat_555_timer_resistor_1 = tk.Label(gui_frm_555_timer, relief='sunken')
gui_stat_555_timer_resistor_1.place(x=95, y=63, width=50, height=20)

gui_lbl_555_timer_resistor_2 = tk.Label(gui_frm_555_timer, text="Resistor 2(Ω):", relief='groove')
gui_lbl_555_timer_resistor_2.place(x=150, y=63, width=95, height=20)
gui_stat_555_timer_resistor_2 = tk.Label(gui_frm_555_timer, relief='sunken')
gui_stat_555_timer_resistor_2.place(x=245, y=63, width=50, height=20)


# Loops... Loops...
root.config(menu=gui_menubar)
root.mainloop()
