import socket
import sys


def main():
    print("-----Menu-----\n1: Play Game\n2: Quit")
    while True:
        answer = input("Enter a choice: ")
        if answer == "1":
            s.send(b"start")
            break
        elif answer == "2":
            s.send(b"quit")
            s.close()
            sys.exit(0)
        else:
            print(answer + " is not an option.")

    print("Waiting for another player...")
    while True:
        x = s.recv(1024).decode("utf-8")
        if x == "found":
            print("Starting game...")
            break

    play_game()


def play_game():
    player_turn = s.recv(1024).decode("utf-8")                          # Receive which player you are
    print(player_turn)
    winner = s.recv(1024).decode("utf-8")                               # Receive winner (True or False)
    turn = ""
    while winner != "True":                                             # Start while loop
        board = s.recv(1024).decode("utf-8")                            # Receive board
        print(board)

        turn = s.recv(1024).decode("utf-8")                             # Receive who's turn it is
        print(turn)

        if turn == "Your Turn":                                         # If it is your turn
            move = input("Enter a choice: ")
            s.send(move.encode())                                       # Send your choice

        winner = s.recv(1024).decode("utf-8")                           # Receive winner (True or False)
                                                                        # End while

    board = s.recv(1024).decode("utf-8")
    print(board)

    if turn == "Your Turn":
        print("You win!")
    else:
        print("They win!")

    main()


def player2():
    print("You are player 2")

    while True:
        board = s.recv(1024).decode("utf-8")
        print(board)

        turn = s.recv(1024).decode("utf-8")
        print(turn)

        if turn == "Your Turn":
            move = input("Enter a choice: ")
            s.send(move.encode())

host = socket.gethostname()
port = 1234

s = socket.socket()
s.connect((host, port))

msg1 = s.recv(1024).decode("utf-8")
print(msg1)

main()

wait = input("Hit any key.")
s.close()
