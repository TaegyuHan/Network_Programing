import socket

address = ("localhost", 8001)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:

    s.send(b"Request")
    data = s.recv(BUFSIZE).decode()
    print(f"Received message: {data}")

s.close()