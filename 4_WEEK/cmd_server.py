from socket import *
import sys

port = 2500
BUFSIZE = 1024

# sys.argv
# 코드 실행할 댸 명령인자가 들어왔는지 확인
if len(sys.argv) > 1:
    port = int(sys.argv[1])

socket = socket(AF_INET, SOCK_STREAM)
socket.bind(("", port))
socket.listen(1)
conn, addr = socket.accept()
print("connected by", addr)

while True:

    data = conn.recv(BUFSIZE)
    if not data:
        break
    print("Received message: ", data.decode())
    conn.send(data)

conn.close()