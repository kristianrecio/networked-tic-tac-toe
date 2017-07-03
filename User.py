import tkinter as tk


class User:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Network Tic-Tac-Toe")
        self.root.geometry('{}x{}'.format(300, 250))  # Dimensions of the GUI

        self.buttons()


    def toggle_text1(self, button):  # This function changes the blank button to what it needs to be

        if button['text'] == "":
            button['text'] = "X"
        elif button['text'] == "X":
            button['text'] = "O"
        else:
            button['text'] = ""

    def buttons(self):
        # These are the buttons for the game
        self.button1 = tk.Button(text="", width=5, height=2, command=lambda: self.toggle_text1(self.button1))
        self.button1.place(relx=.3, rely=.2, anchor="center")

        self.button2 = tk.Button(text="", width=5, height=2, command=lambda: self.toggle_text1(self.button2))
        self.button2.place(relx=.5, rely=.2, anchor="center")

        self.button3 = tk.Button(text="", width=5, height=2, command=lambda: self.toggle_text1(self.button3))
        self.button3.place(relx=.7, rely=.2, anchor="center")

        self.button4 = tk.Button(text="", width=5, height=2, command=lambda: self.toggle_text1(self.button4))
        self.button4.place(relx=.3, rely=.4, anchor="center")

        self.button5 = tk.Button(text="", width=5, height=2, command=lambda: self.toggle_text1(self.button5))
        self.button5.place(relx=.5, rely=.4, anchor="center")

        self.button6 = tk.Button(text="", width=5, height=2, command=lambda: self.toggle_text1(self.button6))
        self.button6.place(relx=.7, rely=.4, anchor="center")

        self.button7 = tk.Button(text="", width=5, height=2, command=lambda: self.toggle_text1(self.button7))
        self.button7.place(relx=.3, rely=.6, anchor="center")

        self.button8 = tk.Button(text="", width=5, height=2, command=lambda: self.toggle_text1(self.button8))
        self.button8.place(relx=.5, rely=.6, anchor="center")

        self.button9 = tk.Button(text="", width=5, height=2, command=lambda: self.toggle_text1(self.button9))
        self.button9.place(relx=.7, rely=.6, anchor="center")

        self.root.mainloop()



                #  1) Change the color of the buttons on each click
                #  2) Create a black bar to mark out the game lines
                #  3) Change the font size

User()


