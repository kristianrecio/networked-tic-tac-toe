import socket
import _thread


def client_connection(client_num):
    print("Hello")
    conn = clients[client_num][0]
    address = clients[client_num][1]
    print("Got connection from", address)
    while True:
        if not clients[client_num][2]:
            message = conn.recv(1).decode("utf-8")
            if message == "T":
                paired.append(clients[client_num])
                clients[client_num][2] = True
                print(clients[client_num][1], "is waiting to play the game.")
            elif message == "F":
                clients[client_num] = None
                conn.close()
                break


def play_game(player1, player2):
    print("Starting a game of Tic Tac Toe")
    print("With", player1[1], "and", player2[1])
    player1[0].send(b"A")
    player2[0].send(b"A")

    choices = []

    for x in range(0, 9):
        choices.append(str(x + 1))

    player1_turn = True
    winner = False
    player1[0].send(b"1")
    player2[0].send(b"2")
    send_winner(winner, player1[0], player2[0])
    while not winner:
        # send_board(choices, player1[0], player2[0])

        if player1_turn:
            choice = player1[0].recv(1024).decode("utf-8")
            choices[int(choice) - 1] = "X"
            player2[0].send(choice.encode())
        else:
            choice = player2[0].recv(1024).decode("utf-8")
            choices[int(choice) - 1] = "O"
            player1[0].send(choice.encode())

        player1_turn = not player1_turn

        for x in range(0, 3):
            y = x * 3
            if choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]:
                winner = True
                send_winner(winner, player1[0], player2[0])
            if choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]:
                winner = True
                send_winner(winner, player1[0], player2[0])

        if ((choices[0] == choices[4] and choices[0] == choices[8]) or
                (choices[2] == choices[4] and choices[4] == choices[6])):
            winner = True
            send_winner(winner, player1[0], player2[0])

        send_winner(winner, player1[0], player2[0])

    if not player1_turn:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    player1[2] = False
    player2[2] = False


def send_winner(winner, conn1, conn2):
    if winner:
        conn1.send(b"T")
        conn2.send(b"T")
    else:
        conn1.send(b"F")
        conn2.send(b"F")


def send_board(choices, conn1, conn2):
    board = "|\n -----\n|" + choices[0] + "|" + choices[1] + "|" + choices[2] + \
            "|\n -----\n|" + choices[3] + "|" + choices[4] + "|" + choices[5] + \
            "|\n -----\n|" + choices[6] + "|" + choices[7] + "|" + choices[8] + \
            "|\n -----\n|"
    conn1.send(board.encode())
    conn2.send(board.encode())


def wait_to_play():
    while True:
        if len(paired) >= 2:
            _thread.start_new_thread(play_game, (paired[0], paired[1]))
            del paired[0]
            del paired[0]


def add_client(client):
    added = False
    pos = None
    for i in range(len(clients)):
        if clients[i] is None:
            clients[i] = client
            pos = i
            added = True
            break

    if not added:
        clients.append(client)
        pos = len(clients) - 1

    return pos


''' START OF THE PROGRAM '''

s = socket.socket()                                         # Creates a socket
host = socket.gethostname()                                 # Gets to the host
port = 1234                                                 # Chooses the port
s.bind((host, port))                                        # Connects to the host through the port

clients = []                                                # List to hold the clients
paired = []                                                 # List to hold clients who want to play the game
_thread.start_new_thread(wait_to_play, ())                  # Starts new thread for wait_to_play function
s.listen(5)                                                 # Listens for clients
while True:                                                 # while True
    c, addr = s.accept()                                    # Accept connection from client
    pos = add_client([c, addr, False])                      # Call add_client function
    _thread.start_new_thread(client_connection, (pos,))     # Starts new thread for client_connection
