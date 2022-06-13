"""
    SSL 에코 클라이언트
"""

import socket
import ssl

PORT = int(input("Port No: "))
BUF_SIZE = 1024
address = ("localhost", PORT)

context = ssl.create_default_context(cafile="root.pem")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_conn = context.wrap_socket(sock, server_hostname="iot.co.kr")
ssl_conn.connect(address)

while True:
    msg = input("Message to send:")
    ssl_conn.send(msg.encode())
    data = ssl_conn.recv(BUF_SIZE)
    print(f"Received message: {data.decode()}")