import tkinter as tk

def toggle_text1(button):  # This function changes the blank button to what it needs to be
    if button['text'] == "":
        button['text'] = "X"
    elif button['text'] == "X":
        button['text'] = "O"
    else:
        button['text'] = ""

#  1) Change the color of the buttons on each click
#  2) Create a black bar to mark out the game lines
#  3) Change the font size

root = tk.Tk()
root.title("Network Tic-Tac-Toe")
root.geometry('{}x{}'.format(300, 250))  # Dimensions of the GUI

# These are the buttons for the game
button1 = tk.Button(text="", width=5, height=2, command=lambda: toggle_text1(button1))
button1.place(relx=.3, rely=.2, anchor="center")

button2 = tk.Button(text="", width=5, height=2, command=lambda: toggle_text1(button2))
button2.place(relx=.5, rely=.2, anchor="center")

button3 = tk.Button(text="", width=5, height=2, command=lambda: toggle_text1(button3))
button3.place(relx=.7, rely=.2, anchor="center")

button4 = tk.Button(text="", width=5, height=2, command=lambda: toggle_text1(button4))
button4.place(relx=.3, rely=.4, anchor="center")

button5 = tk.Button(text="", width=5, height=2, command=lambda: toggle_text1(button5))
button5.place(relx=.5, rely=.4, anchor="center")

button6 = tk.Button(text="", width=5, height=2, command=lambda: toggle_text1(button6))
button6.place(relx=.7, rely=.4, anchor="center")

button7 = tk.Button(text="", width=5, height=2, command=lambda: toggle_text1(button7))
button7.place(relx=.3, rely=.6, anchor="center")

button8 = tk.Button(text="", width=5, height=2, command=lambda: toggle_text1(button8))
button8.place(relx=.5, rely=.6, anchor="center")

button9 = tk.Button(text="", width=5, height=2, command=lambda: toggle_text1(button9))
button9.place(relx=.7, rely=.6, anchor="center")

root.mainloop()
