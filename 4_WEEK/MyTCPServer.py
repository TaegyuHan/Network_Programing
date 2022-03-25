import socket


class TCPServer:
    """
        TCP 클래스 사용
    """

    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("", port))
        self.sock.listen(5)

    def accept(self):
        self.c_sock, self.c_addr = self.sock.accept()
        return self.c_sock, self.c_addr


if __name__ == '__main__':
    sock = TCPServer(8888)
    c, addr = sock.accept()
    print("connceted by ", addr)
    c.send(b"Hello Client")
    c.close()