from socket import *

BUFSIZE = 1024

s = socket.create_server(("localhost", 2500))

while True:
    msg = input("Message to send: ")
    s.send(msg.encode())
    data = s.recv(BUFSIZE)
    if not data:
        break
    print(f"Received message: {data.decoede()}")

s.close()