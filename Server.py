# Server Class

import socket


class Server:
    s = socket.socket()
    host = socket.gethostname()
    port = 1234
    s.bind((host, port))

    s.listen(5)
    while True:
        c, addr = s.accept()
        print("Got connection from", addr)
        c.send(b"Thank you for connecting")
        c.close()