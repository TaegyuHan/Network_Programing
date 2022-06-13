"""
    SSL 에코 서버
"""

from socket import *
import ssl

PORT = 2500
BUF_SIZE = 1024

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

# 서버 인증서와 개인키 설정
context.load_cert_chain(certfile="server.pem", keyfile="server.key")

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("", PORT))
sock.listen(1)

ssl_sock = context.wrap_socket(sock, server_side=True)
ssl_conn, (remotehost, remoteport) = ssl_sock.accept()
print("connected by", remotehost, remoteport)

while True:
    data = ssl_conn.recv(BUF_SIZE)
    print("Received message: ", data.decode())
    ssl_conn.send(data)