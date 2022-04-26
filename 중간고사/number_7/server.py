import selectors
from socket import *

class Sockets:
    """ 다른 사용자들 """
    LIST = []

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()
    print("new client", addr)
    Sockets.LIST.append(conn)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)
    if not data:
        sel.unregister(conn)
        conn.close()
        return

    # 다른사람 에게 보내기
    for other_socket in Sockets.LIST:
        other_socket.send(data)
    print("received data:", data.decode())

sock = socket()
sock.bind(("", 2500))
sock.listen(5)

sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)