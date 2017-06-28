import socket

host = socket.gethostname()
port = 1234

s = socket.socket()
s.connect((host, port))


print("Connected to the server.")
answer = input("Play game (y/n)? ")

if answer in ['y', 'Y']:
    s.send(b"start")
    print("Playing game..")
    answer = 'n'
    while answer in ['n', 'N']:
        answer = input("Stop playing (y/n)? ")
    s.close()
else:
    s.send(b"quit")

s.close()
