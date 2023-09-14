"""
Name: Aaron Mark William
Student id: S240132

Additional notes:
Included text version of vending machine (s240132_tx_main_041122.py) as reference of a text implementation of the assessment.
Included version (s240132_vm_031222.py) as reference - as it shows more robust coding, but ultimately unfinished.
"""
# ============================================
#: 1.0 Imports

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

# ============================================
#: 1.1 Main Frame

vending_main = tk.Tk()
vending_main.configure(bg='#1e16af')
vending_main.title("Marvelous Mini Munchie Machine")
vending_main.geometry('365x150')
# ============================================
#: 1.2 Fonts and colour
t_h1 = 'Arial 10 bold'
t_h2 = 'Arial 14 bold'
t_h3 = 'Arial 12 bold'
t_b1 = 'Arial 12'
t_b2 = 'Arial 10'

colour_background = '#1e16af'
colour_secondary = '#ff9200'
colour_accent = '#d8a757'
colour_text_main = '#FFFFFF'
colour_text_secondary = '#000000'
# ============================================
#: 1.3 Left and right frame
left_frame = Frame(vending_main, width=200, height=250)
left_frame.configure(height=250, background=colour_secondary)
left_frame.grid(row=0, column=0, ipady=20)

right_frame = Frame(vending_main, width=200, height=250)
right_frame.configure(bg=colour_background)
right_frame.grid(row=0, column=1, padx=5)
# ============================================
#: 2.0 Global var and moving text

global balance
balance = 0
moving_text = '________'
# ============================================
#: 2.1 Content

options = {'Twin Bar': '50p', 'Mar Bar': '20p', 'Far Bar': '10p', 'Slim Bar': '5p'}
message = ['insert a coin', 'choose a candy bar', 'coin accepted', 'current balance: ', 'Transaction cancelled']
# ============================================
#: 2.2 Functions

#: 2.2.1 Balance Processing
"""First we call the global variable balance, then we take the value from the
Combobox choice and update the value in balance to the result. Because it has the 'p' in it,
it is a string type. In order to be able to further use the balance in other functions we remove the letter 'p'
using the replace method, then using the int() we change 'balance' into an integer."""


def balance_processing1():
    global balance
    balance = dropdown_menu.get()
    balance = int(balance.replace('p', ''))


#: 2.2.2 Balance Processing 2
"""This function is similar to what we've done in balance_processing1, but this time we are setting the
variable 'choice' to the chosen candy bar. This is now our key. then we use .get to find the value
 of the dict entry. The values are candy bar prices. We then update the balance by processing the
 price in a similar way to above, then we subtract choice from balance and updating the balance from there."""


def balance_processing2():
    global balance
    choice = dropdown_menu.get()
    choice = int(options.get(choice).replace('p', ''))
    balance = balance - choice


#: 2.2.3 Updating Options
"""Using if and elif statements to filter out the candy bars to only show ones that the user can afford."""

"""candy_list defined as an empty list. We are using extend instead of append
so that we are adding values as separate items in a list."""


def update_options():
    candy_list = []
    if balance >= 50:
        candy_list.extend(['Twin Bar', 'Mar Bar', 'Far Bar', 'Slim Bar'])
        dropdown_menu.set('Twin Bar')
    elif balance >= 20:
        candy_list.extend(['Mar Bar', 'Far Bar', 'Slim Bar'])
        dropdown_menu.set('Mar Bar')
    elif balance >= 10:
        candy_list.extend(['Far Bar', 'Slim Bar'])
        dropdown_menu.set('Far Bar')
    elif balance >= 5:
        candy_list.extend(['Slim Bar'])
        dropdown_menu.set('Slim Bar')
    else:
        candy_list.extend([''])
    dropdown_menu['values'] = candy_list
    # _ if balance is 0, make button inactive
    if balance <= 0:
        dropdown_menu.set('Insufficient Balance')
        button_confirm.configure(state='disabled')
        button_cancel.configure(text='Quit', command=lambda: close())

    else:
        pass


#: 2.2.4 Update instructions
def update_instructions():
    show_instructions.configure(font=t_h3, text=message[1].upper())


#: 2.2.5 Update balance
"""This is where I set the different processing methods for the starting state for when the balance is 0, or if
the balance is more than 0."""


def coin_add_balance():
    if balance == 0:
        balance_processing1()
        show_balance.configure(text=f'{message[3]}{balance}p')

    elif balance > 0:
        balance_processing2()
        show_balance.configure(text=f'{message[3]}{balance}p')


#: 2.2.6 Change button function groups
def change_button():
    button_confirm.configure(command=lambda: confirm_2())


#: 2.2.7 function groups
"""I am using function groups because while I can call multiple functions from button presses with ([func1],[func2]).
This way is far neater and easier to modify."""


def confirm_1():
    coin_add_balance()
    update_options()
    update_instructions()
    change_button()
    status_confirm()


def confirm_2():
    coin_add_balance()
    status_candy()
    update_options()


def cancel():
    cancel_message()
    close()


def status_confirm():
    messagebox.showinfo('Transaction Confirmed', f'Confirmed!\nCurrent Balance: {balance}p')


def status_candy():
    messagebox.showinfo('Dispensing', f'Current balance:{balance}p\nDispensing: {dropdown_menu.get()}')


def close():
    messagebox.showinfo('Transaction Complete', 'Thank you.')
    vending_main.destroy()


def cancel_message():
    if balance == 0:
        messagebox.showinfo('Transaction Cancelled', 'Transaction Cancelled')
    else:
        messagebox.showinfo('Transaction Cancelled', f'Transaction Cancelled\nReturning: {balance}p')
# ============================================
#: 2.3 Labels


pad = Label(left_frame, text='_________', bg=colour_secondary)

prices = Label(left_frame, text='TWIN BAR | 50p\nMAR BAR | 20p\n'
                                'FAR BAR | 10p\nSLIM BAR | 5p\n_________', font=t_h1,
               bg=colour_secondary, fg=colour_text_secondary)

show_instructions = Label(right_frame, font=t_h2, text=message[0].upper(), bg=colour_background,
                          fg=colour_text_main)
show_balance = Label(left_frame, font=t_b1, text=message[3].lower(), bg=colour_secondary, fg=colour_text_main)
# ============================================
#: 2.4 Dropdown
"""This Combobox takes the values from the options dictionary, uses the 'list' attribute to turn the result of
.values() into a list, which is treated as separate choices by Combobox."""
dropdown_menu = ttk.Combobox(right_frame, font=t_b1, values=list(options.values()), state='readonly')
dropdown_menu.set('50p')
# ============================================
#: 2.5 Buttons
"""The main driver of this program, the confirm button uses lambda to pass the data to a callback function."""
button_confirm = tk.Button(right_frame, font=t_h2, bg=colour_secondary, fg=colour_background, bd=0, text='Confirm',
                           command=lambda: confirm_1())

button_cancel = tk.Button(right_frame, font=t_h2, bg=colour_secondary, fg=colour_background,
                          bd=0, text='Cancel', command=lambda: cancel())
# ============================================
#: 3.0 Widget grids and padding
#: Left Frame (0 is top)
pad.grid(row=0, column=0)
prices.grid(row=1, column=0, padx=0, pady=0, ipadx=25, sticky='')
show_balance.grid(row=2, column=0, padx=0, pady=3, sticky='')
#: Right Frame (0 is top)
show_instructions.grid(row=0, column=0, ipadx=0, padx=0, pady=9, columnspan=2, sticky='n')
dropdown_menu.grid(row=1, column=0, padx=0, pady=0, columnspan=2, sticky='')
button_confirm.grid(row=2, column=0, padx=5, pady=2, columnspan=2, sticky='w')
button_cancel.grid(row=2, column=1, padx=5, pady=2, columnspan=2, sticky='e')
# ============================================
#: 4.0 Mainloop
"""Setting resizable to false to prevent the program from resizing."""
vending_main.resizable(False, False)
vending_main.mainloop()

"""
_______________References_______________
Ahmad, Nasreen. (2015) Finite State Vending Machine, Formal Methods Engineering, pp. 2-36.

Aksel2099. et al (2018) How to make buttons FLAT on Tkinter GUI? Available at
https://stackoverflow.com/questions/50367083/how-to-make-buttons-flat-on-tkinter-gui (Accessed 02 November 2022)

Caterin. et al (2022) How do you set functions for a button, on Tkinter? Available at
https://stackoverflow.com/questions/74248108/how-do-you-set-functions-for-a-button-on-tkinter
(Accessed 02 November 2022)

Geek for geeks (no date) Python Dictionary Values. Available at
https://www.geeksforgeeks.org/python-dictionary-values/ (Accessed 09 October 2022)

Geek for geeks (no date) Python Key Index in Dictionary. Available at
https://www.geeksforgeeks.org/python-key-index-in-dictionary/ (Accessed 09 October 2022)

Programiz (no date) Python Dictionary. Available at:
https://www.programiz.com/python-programming/dictionary (Accessed: 03 October 2022).

Python.org (2022) Built-in Types. Available at:
https://docs.python.org/3.9/library/stdtypes.html#dict.keys (Accessed: 03 October 2022).

Python Enhancement Proposals (2003) Generator Expressions. Available at:
https://peps.python.org/pep-0289/ (Accessed: 04 October 2022).

Python Programming (no date) Tkinter Intro. Available at:
https://pythonprogramming.net/python-3-tkinter-basics-tutorial/ (Accessed 04 October 2022).

Rohit (2018) Python Comments Block Syntax | Multiline Comment with Examples. Available at
https://tutorial.eyehunts.com/python/python-comments-block-syntax-multiline-example/ (Accessed 03 November 2022)

Starspiker. et al (2018) Comparing a value to multiple values in a list. Available at
https://stackoverflow.com/questions/49102211/comparing-a-value-to-multiple-values-in-a-list (Accessed: 04 October 2022).

Stefansfan (2017) Design a vending machine. Available at
https://leetcode.com/discuss/interview-question/object-oriented-design/125218/design-a-vending-machine
(Accessed 10 October 2022)

What is a state machine? (no date) Available at
https://www.itemis.com/en/yakindu/state-machine/documentation/user-guide/overview_what_are_state_machines
(Accessed 09 October 2022)
"""
