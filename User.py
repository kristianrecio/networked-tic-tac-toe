import tkinter as tk

class MainWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(1, weight=10)
        container.grid_columnconfigure(1, weight=10)

        self.frames = {}
        for F in (Start, User, Wait):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Start")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class Start(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page")
        label.pack(side="top", fill="x", pady=100, padx=100)

        # This button goes to the User frame
        user = tk.Button(self, text="Start", command=lambda: controller.show_frame("User"))
        quits = tk.Button(self, text="Quit", command=lambda: controller.quit())  # This quits the program
        user.place(relx=.4, rely=.7, anchor="center")
        quits.place(relx=.6, rely=.7, anchor="center")


class User(tk.Frame):  # This is the user windows

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Tic-Tac-Toe")
        label.pack(side="top", fill="x", pady=100, padx=100)

        def toggle_text1(button):  # This function changes the blank button to what it needs to be
            if button['text'] == "":
                button['text'] = "X"
            elif button['text'] == "X":
                button['text'] = "O"
            else:
                button['text'] = ""

        def buttons(): # These are the buttons for the game
            button1 = tk.Button(text="", width=5, height=2, command=lambda: controller.toggle_text1(button1))
            button1.place(relx=.3, rely=.2, anchor="center")

            button2 = tk.Button(text="", width=5, height=2, command=lambda: controller.toggle_text1(button2))
            button2.place(relx=.5, rely=.2, anchor="center")

            button3 = tk.Button(text="", width=5, height=2, command=lambda: controller.toggle_text1(button3))
            button3.place(relx=.7, rely=.2, anchor="center")

            button4 = tk.Button(text="", width=5, height=2, command=lambda: controller.toggle_text1(button4))
            button4.place(relx=.3, rely=.4, anchor="center")

            button5 = tk.Button(text="", width=5, height=2, command=lambda: controller.toggle_text1(button5))
            button5.place(relx=.5, rely=.4, anchor="center")

            button6 = tk.Button(text="", width=5, height=2, command=lambda: controller.toggle_text1(button6))
            button6.place(relx=.7, rely=.4, anchor="center")

            button7 = tk.Button(text="", width=5, height=2, command=lambda: controller.toggle_text1(button7))
            button7.place(relx=.3, rely=.6, anchor="center")

            button8 = tk.Button(text="", width=5, height=2, command=lambda: controller.toggle_text1(button8))
            button8.place(relx=.5, rely=.6, anchor="center")

            button9 = tk.Button(text="", width=5, height=2, command=lambda: controller.toggle_text1(button9))
            button9.place(relx=.7, rely=.6, anchor="center")

            submit = tk.Button(self, text="Submit", command=lambda: controller.show_frame("Wait"))
            submit.place(relx=.5, rely=.8, anchor="center")  # This button goes to the Wait frame

        buttons()


class Wait(tk.Frame):  # This window waits for the other player to submit

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please waiting for other player")
        label.pack(side="top", fill="x", pady=100, padx=100)
        start = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("Start"))
        start.place(relx=.5, rely=.7, anchor="center")


MainWindow().mainloop()
