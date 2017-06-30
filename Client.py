import socket
import sys


def main():                                                 # Main function
    print("-----Menu-----\n1: Play Game\n2: Quit")          # Prints out menu to client
    while True:                                             # while True
        answer = input("Enter a choice: ")                  #   Prompts client for a choice
        if answer == "1":                                   #       If client chooses 1
            s.send(b"start")                                #           Sends to the server "start"
            break                                           #           breaks out of while loop
        elif answer == "2":                                 #       Elif client chooses 2
            s.send(b"quit")                                 #           Sends to the server "quit"
            s.close()                                       #           Closes connection
            sys.exit(0)                                     #           Closes the program
        else:                                               #       Else
            print(answer + " is not an option.")            #           Prints out input was invalid

    print("Waiting for another player...")                  # Prints out waiting for another player
    while True:                                             # while True
        x = s.recv(1024).decode("utf-8")                    # Waits to receive string from server
        if x == "found":                                    # If received string is "found"
            print("Starting game...")                       #   Print outs "Starting game"
            break                                           #   Breaks out of while loop

    play_game()                                             # Calls play_game function


def play_game():                                            # Play game function
    player_turn = s.recv(1024).decode("utf-8")              # Receive which player you are
    print(player_turn)                                      # Prints out which player you are
    winner = s.recv(1024).decode("utf-8")                   # Receive winner will always be False
    turn = ""                                               # Initializes turn
    while winner != "True":                                 # while there is no winner
        board = s.recv(1024).decode("utf-8")                #   Receive board from server
        print(board)                                        #   Print the board

        turn = s.recv(1024).decode("utf-8")                 #   Receive who's turn it is
        print(turn)                                         #   Print out who's turn it is

        if turn == "Your Turn":                             #   If it is your turn
            move = input("Enter a choice: ")                #       Prompts client for choice
            s.send(move.encode())                           #       Sends choice the server

        winner = s.recv(1024).decode("utf-8")               # Receive winner (True or False)

    board = s.recv(1024).decode("utf-8")                    # Receive board from server
    print(board)                                            # Prints out the board

    if turn == "Your Turn":                                 # If it was your turn
        print("You win!")                                   #   Prints out you win!
    else:                                                   # Else
        print("They win!")                                  #   Prints out they win!

    main()                                                  # Calls the main function (Recursion)

'''
START OF THE PROGRAM
'''

host = socket.gethostname()                                 # Server part
port = 1234
s = socket.socket()
s.connect((host, port))

main()
