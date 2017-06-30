import tkinter as tk
from tkinter import *

def toggle_text1(button):  # This function changes the blank button to what it needs to be
    if button['text'] == "":
        button['text'] = "X"
    elif button['text'] == "X":
        button['text'] = "O"
    else:
        button['text'] = ""

#These are the buttons for the game
root = tk.Tk()
root.title("Network Tic-Tac-Toe")
button1 = tk.Button(text="", width=5, command= lambda : toggle_text1(button1))
button1.grid(row=1, column=1, padx=5, pady=5, sticky=E)

button2 = tk.Button(text="", width=5, command= lambda : toggle_text1(button2))
button2.grid(row=1, column=2, padx=5, pady=5, sticky=E)

button3 = tk.Button(text="", width=5, command= lambda : toggle_text1(button3))
button3.grid(row=1, column=3, padx=5, pady=5, sticky=E)

button4 = tk.Button(text="", width=5, command= lambda : toggle_text1(button4))
button4.grid(row=2, column=1, padx=5, pady=5, sticky=E)

button5 = tk.Button(text="", width=5, command= lambda : toggle_text1(button5))
button5.grid(row=2, column=2, padx=5, pady=5, sticky=E)

button6 = tk.Button(text="", width=5, command= lambda : toggle_text1(button6))
button6.grid(row=2, column=3, padx=5, pady=5, sticky=E)

button7 = tk.Button(text="", width=5, command= lambda : toggle_text1(button7))
button7.grid(row=3, column=1, padx=5, pady=5, sticky=E)

button8 = tk.Button(text="", width=5, command= lambda : toggle_text1(button8))
button8.grid(row=3, column=2, padx=5, pady=5, sticky=E)

button9 = tk.Button(text="", width=5, command= lambda : toggle_text1(button9))
button9.grid(row=3, column=3, padx=5, pady=5, sticky=E)

root.mainloop()
