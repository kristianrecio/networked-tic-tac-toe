import tkinter as tk
import socket
import _thread


class MainWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        self.title("Network Tic-Tac-Toe")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(1, weight=10)
        container.grid_columnconfigure(1, weight=10)

        self.frames = {}
        for F in (Start, User, Wait, Result):
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
        label = tk.Label(self, text="Welcome to Network Tic-Tac-Toe")
        label.pack(side="top", fill="x", pady=100, padx=100)

        # This button goes to the User frame
        user = tk.Button(self, text="Start", command=lambda: [controller.show_frame("Wait"), s.send(b"T"), _thread.start_new_thread(self.waiting, ())])
        quits = tk.Button(self, text="Quit", command=lambda: [controller.quit(), s.send(b"F")])  # This quits the program
        user.place(relx=.4, rely=.7, anchor="center")
        quits.place(relx=.6, rely=.7, anchor="center")

    def waiting(self):
        while True:  # while True
            x = s.recv(1).decode("utf-8")  # Waits to receive string from server
            print("X:", x)
            if x == "A":  # If received string is "found"
                self.controller.show_frame("User")
                break
        global player
        player = int(s.recv(1).decode("utf-8"))
        print("Player:", str(player))
        if player == 1:
            global turn
            turn = 1
        global winner
        winner = s.recv(1).decode("utf-8")
        print("Winner:", winner)


class User(tk.Frame):  # This is the user windows
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.move = ""
        # label = tk.Label(self, text="")
        # label.pack(side="top", fill="x", pady=100, padx=100)

        self.player_label = tk.Label(self)
        self.player_label.place(relx=.1, rely=.2, anchor="center")
        self.wait_label = tk.Label(self)
        self.wait_label.place(relx=.5, rely=.9, anchor="center")
        self.button_list = []
        self.buttons()

        _thread.start_new_thread(self.listen_for_move, ())
        _thread.start_new_thread(self.listen_for_winner, ())

    def toggle_text(self, button):  # This function changes the blank button to what it needs to be
        global player

        for i in self.button_list:
            if i['state'] == 'disabled':
                continue
            else:
                i['text'] = ""

        button['text'] = "X" if player == 1 else "O"

    def set_move(self, move):
        self.move = move

    def buttons(self):  # These are the buttons for the game
        self.button1 = tk.Button(self, text="", width=5, height=2, command=lambda: [self.toggle_text(self.button1), self.set_move("1")])
        self.button1.place(relx=.3, rely=.2, anchor="center")
        self.button_list.append(self.button1)

        self.button2 = tk.Button(self, text="", width=5, height=2, command=lambda: [self.toggle_text(self.button2), self.set_move("2")])
        self.button2.place(relx=.5, rely=.2, anchor="center")
        self.button_list.append(self.button2)

        self.button3 = tk.Button(self, text="", width=5, height=2, command=lambda: [self.toggle_text(self.button3), self.set_move("3")])
        self.button3.place(relx=.7, rely=.2, anchor="center")
        self.button_list.append(self.button3)

        self.button4 = tk.Button(self, text="", width=5, height=2, command=lambda: [self.toggle_text(self.button4), self.set_move("4")])
        self.button4.place(relx=.3, rely=.4, anchor="center")
        self.button_list.append(self.button4)

        self.button5 = tk.Button(self, text="", width=5, height=2, command=lambda: [self.toggle_text(self.button5), self.set_move("5")])
        self.button5.place(relx=.5, rely=.4, anchor="center")
        self.button_list.append(self.button5)

        self.button6 = tk.Button(self, text="", width=5, height=2, command=lambda: [self.toggle_text(self.button6), self.set_move("6")])
        self.button6.place(relx=.7, rely=.4, anchor="center")
        self.button_list.append(self.button6)

        self.button7 = tk.Button(self, text="", width=5, height=2, command=lambda: [self.toggle_text(self.button7), self.set_move("7")])
        self.button7.place(relx=.3, rely=.6, anchor="center")
        self.button_list.append(self.button7)

        self.button8 = tk.Button(self, text="", width=5, height=2, command=lambda: [self.toggle_text(self.button8), self.set_move("8")])
        self.button8.place(relx=.5, rely=.6, anchor="center")
        self.button_list.append(self.button8)

        self.button9 = tk.Button(self, text="", width=5, height=2, command=lambda: [self.toggle_text(self.button9), self.set_move("9")])
        self.button9.place(relx=.7, rely=.6, anchor="center")
        self.button_list.append(self.button9)

        self.submit = tk.Button(self, text="Submit", command=lambda: self.send_move())
        self.submit.place(relx=.5, rely=.8, anchor="center")  # This button goes to the Wait frame

    def send_move(self):
        global turn
        if turn == 1 and self.move != "":
            s.send(self.move.encode())
            for i in range(len(self.button_list) + 1):
                if str(i) == self.move:
                    self.set_button(self.button_list[i - 1], 1)
                    break
            turn = 0

    def listen_for_move(self):
        while True:
            if player == 0:
                continue
            self.player_label['text'] = "Player " + str(player)

            while True:
                global turn
                global winner
                if turn == 1:
                    continue
                else:
                    self.submit['state'] = 'disabled'
                    self.wait_label['text'] = "Waiting for other player"
                    if winner == "T":
                        break
                    pos = s.recv(1).decode("utf-8")
                    print("pos:", pos)
                    if pos == "1":
                        self.set_button(self.button1, 2)
                    elif pos == "2":
                        self.set_button(self.button2, 2)
                    elif pos == "3":
                        self.set_button(self.button3, 2)
                    elif pos == "4":
                        self.set_button(self.button4, 2)
                    elif pos == "5":
                        self.set_button(self.button5, 2)
                    elif pos == "6":
                        self.set_button(self.button6, 2)
                    elif pos == "7":
                        self.set_button(self.button7, 2)
                    elif pos == "8":
                        self.set_button(self.button8, 2)
                    elif pos == "9":
                        self.set_button(self.button9, 2)
                    winner = s.recv(1).decode("utf-8")
                    print("Winner:", winner)
                    turn = 1
                    self.wait_label['text'] = ""
                    self.submit['state'] = 'normal'
                if winner == "T":
                    global player
                    player = 0
                    break

    def listen_for_winner(self):
        while True:
            if player == 0:
                continue

            global turn
            while True:
                if turn == 0:
                    continue
                else:
                    global winner
                    winner = s.recv(1).decode("utf-8")
                    print("Winner:", winner)
                    if winner == "T":
                        print("There was a winner")
                        for i in self.button_list:
                            i['state'] = 'disabled'
                        self.submit['state'] = 'disabled'
                        self.reset_button()
                        self.controller.show_frame("Result")
                        global player
                        player = 0
                        break
                    turn = 0

    def reset_button(self):
        for i in self.button_list:
            i['text'] = ""
            i['state'] = "normal"

    @staticmethod
    def set_button(button, who):
        global player
        if who == 1:
            button['text'] = "X" if player == 1 else "O"
            button['state'] = 'disabled'
        else:
            button['text'] = "X" if player == 2 else "O"
            button['state'] = 'disabled'


class Wait(tk.Frame):  # This window waits for the other player to submit
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        print("Here already")
        label = tk.Label(self, text="Please waiting for other player")
        label.pack(side="top", fill="x", pady=100, padx=100)


class Result(tk.Frame):  # This window waits for the other player to submit
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        print("Here already")
        label = tk.Label(self, text="Winner winner chicken dinner play[i] wins")
        label.pack(side="top", fill="x", pady=100, padx=100)
        label = tk.Label(self, text="Do you want to play again?")
        label.place(relx=.6, rely=.4, anchor="center")
        user = tk.Button(self, text="Play Again", command=lambda: [controller.show_frame("Wait"), s.send(b"T"), _thread.start_new_thread(self.waiting, ())])
        quits = tk.Button(self, text="Quit", command=lambda: [controller.quit(), s.send(b"F")])  # This quits the program
        user.place(relx=.4, rely=.7, anchor="center")
        quits.place(relx=.6, rely=.7, anchor="center")

    def waiting(self):
        while True:  # while True
            x = s.recv(1).decode("utf-8")  # Waits to receive string from server
            print("X: ", x)
            if x == "A":  # If received string is "found"
                self.controller.show_frame("User")
                break
        global player
        player = int(s.recv(1).decode("utf-8"))
        print("Player:", str(player))
        if player == 1:
            global turn
            turn = 1
        global winner
        winner = s.recv(1).decode("utf-8")
        print("Winner:", winner)

host = socket.gethostname()  # Server part
port = 1234
s = socket.socket()
s.connect((host, port))
player = 0
turn = 0
winner = ""

MainWindow().mainloop()
