from socket import *

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(("", port))

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    print("<- ", data.decode())
    resp = input("-> ")
    sock.sendto(resp.encode(), addr)
