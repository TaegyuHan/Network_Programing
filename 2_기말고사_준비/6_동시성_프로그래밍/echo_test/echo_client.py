"""
    멀티스레드 에코 클라이언트
"""
from socket import *

if __name__ == '__main__':
    """ 메시지 전송 클라이언트 """
    port = int(input("Port No: "))
    address = ("localhost", port)
    BUF_SIZE = 1024


    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(address)

    while True:
        msg = input("Message to send: ")
        sock.send(msg.encode())
        data = sock.recv(BUF_SIZE)
        if not data:
            break
        print(f"Received message: {data.decode()}")

    sock.close()
