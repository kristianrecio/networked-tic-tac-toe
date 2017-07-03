import socket
import _thread


def client_connection(client_num):
    print("Hello")
    conn = clients[client_num][0]
    address = clients[client_num][1]
    print("Got connection from", address)
    while True:
        if not clients[client_num][2]:
            message = conn.recv(1024).decode("utf-8")
            if message == "start":
                paired.append(clients[client_num])
                clients[client_num][2] = True
            elif message == "quit":
                clients[client_num] = None
                conn.close()
                break


def play_game(player1, player2):
    print("Starting a game of Tic Tac Toe")
    print("With", player1[1], "and", player2[1])
    player1[0].send(b"found")
    player2[0].send(b"found")

    choices = []

    for x in range(0, 9):
        choices.append(str(x + 1))

    player1_turn = True
    winner = False
    player1[0].send(b"You are player 1")
    player2[0].send(b"You are player 2")
    send_winner(winner, player1[0], player2[0])
    while not winner:
        send_board(choices, player1[0], player2[0])

        if player1_turn:
            player1[0].send(b"Your Turn")
            player2[0].send(b"Player 1's Turn")
            while True:
                choice = player1[0].recv(1024).decode("utf-8")
                if choices[int(choice) - 1] == "X" or choices[int(choice) - 1] == "O":
                    print("Invalid move. Try again.")
                    player1[0].send(b"Invalid")
                else:
                    choices[int(choice) - 1] = "X"
                    player1[0].send(b"Valid")
                    break
        else:
            player1[0].send(b"Player 2's Turn")
            player2[0].send(b"Your Turn")
            while True:
                choice = player2[0].recv(1024).decode("utf-8")
                if choices[int(choice) - 1] == "X" or choices[int(choice) - 1] == "O":
                    player2[0].send(b"Invalid")
                else:
                    choices[int(choice) - 1] = "O"
                    player2[0].send(b"Valid")
                    break

        player1_turn = not player1_turn

        for x in range(0, 3):
            y = x * 3
            if choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]:
                winner = True
                send_winner(winner, player1[0], player2[0])
                send_board(choices, player1[0], player2[0])
            if choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]:
                winner = True
                send_winner(winner, player1[0], player2[0])
                send_board(choices, player1[0], player2[0])

        if ((choices[0] == choices[4] and choices[0] == choices[8]) or
                (choices[2] == choices[4] and choices[4] == choices[6])):
            winner = True
            send_winner(winner, player1[0], player2[0])
            send_board(choices, player1[0], player2[0])

        send_winner(winner, player1[0], player2[0])

    if not player1_turn:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    player1[2] = False
    player2[2] = False


def send_winner(winner, conn1, conn2):
    conn1.send(str(winner).encode())
    conn2.send(str(winner).encode())


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

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))

clients = []
paired = []
_thread.start_new_thread(wait_to_play, ())
s.listen(5)
while True:
    c, addr = s.accept()
    pos = add_client([c, addr, False])
    _thread.start_new_thread(client_connection, (pos,))
