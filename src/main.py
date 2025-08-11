'''
    Title: CircuitSolver GUI
    Version: 0.1.0

    Formulas By: PseudoSinusoidal
    Graphics By: Floppy

    Started: 2025-08-10
    Updated: 2025-08-10

    Variable Naming Convention:
    gui_  : Anything (and I mean ANYTHING) in the window (goes first)
    btn_  : A button duh
    lbl_  : Label
    ent_  : Entry
    txt_  : Textbox
    stat_ : Status Text
    spin_ : Spinbox
    chk_  : Checkbutton/Checkbox
    sep_  : Separator

    gui_  : Anything (and I mean ANYTHING) in the window (goes first)
    btn_  : A button, duh
    fun_  : Function
    sep_  : Separator
    frm_  : Frame

    Example:
    gui_lbl_blank_blank_sep
    gui_btn_blank
    gui_txt_blank_blank
'''

# ========== Setup ========== #
# Imports
import tkinter as tk

# Tkinter setup
root = tk.Tk()
root.geometry('750x400')
root.title('CircuitSolver GUI - Version: 0.1.0')
# root.iconbitmap(r'../res/circuit_solver_gui_icon.ico')


# ========== Functions ========== #
def do_nothing():
    print("I was pressed!")
    # I'm a placeholder!


# ========== Main Window ========== #
# Menubar
gui_menubar = tk.Menu()

# File menu
gui_file_menu = tk.Menu(gui_menubar, tearoff=False)  # Create file menu
gui_menubar.add_cascade(menu=gui_file_menu, label="File")  # Add a cascade
gui_file_menu.add_command(label="New", command=do_nothing)  # Add a command
gui_file_menu.add_separator()  # Add a separator
gui_file_menu.add_command(label="Exit", command=root.destroy)


# Calculator menu
gui_calculator_menu = tk.Menu(gui_menubar, tearoff=False)
gui_menubar.add_cascade(menu=gui_calculator_menu, label="Calculators")
gui_calculator_menu.add_command(label="555 Timer", command=do_nothing)
gui_calculator_menu.add_command(label="Resistor Values", command=do_nothing)
gui_calculator_menu.add_command(label="Ohm's Law", command=do_nothing)


# 555 timer frame (NOTE: Put into library later on!)
gui_frm_555_timer = tk.Frame(root, width=750, height=400)
gui_frm_555_timer.place(x=0, y=0)

gui_btn_555_timer_input1 = tk.Button(gui_frm_555_timer, text="Input1")
gui_btn_555_timer_input1.place(x=0, y=0, width=50, height=25)
gui_btn_555_timer_input2 = tk.Button(gui_frm_555_timer, text="Input2")
gui_btn_555_timer_input2.place(x=0, y=25, width=50, height=25)
gui_btn_555_timer_input3 = tk.Button(gui_frm_555_timer, text="Input3")
gui_btn_555_timer_input3.place(x=0, y=50, width=50, height=25)
gui_btn_555_timer_solve = tk.Button(gui_frm_555_timer, text="Solve")
gui_btn_555_timer_solve.place(x=0, y=75, width=50, height=25)


# Loops... Loops...
root.config(menu=gui_menubar)
root.mainloop()
