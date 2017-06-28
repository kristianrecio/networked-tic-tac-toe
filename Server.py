# Server Class

import socket
import _thread


def client_connection(client_num):
    print("Hello")
    conn = clients[client_num][0]
    address = clients[client_num][1]
    print("Got connection from", address)
    while True:
        message = conn.recv(1024).decode("utf-8")
        if message == "start":
            clients[client_num][2] = True
            break
        elif message == "stop":
            clients[client_num][2] = False
            break
        elif message == "quit":
            clients.remove(client_num)
            conn.close()
            break


def play_game(player1, player2):
    print("Starting a game of Tic Tac Toe")
    print("With", player1[1], "and", player2[1])
    conn1 = player1[0]
    conn2 = player2[0]


def wait_to_play():
    paired = []
    while True:
        for i in clients:
            if i[2]:
                paired.append(i)
                clients.remove(i)
            else:
                if i in paired:
                    paired.remove(i)
            if len(paired) == 2:
                _thread.start_new_thread(play_game, (paired[0], paired[1]))
                paired = []

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))

clients = []
_thread.start_new_thread(wait_to_play, ())
s.listen(5)
while True:
    c, addr = s.accept()
    clients.append([c, addr, False])
    _thread.start_new_thread(client_connection, (len(clients) - 1,))


