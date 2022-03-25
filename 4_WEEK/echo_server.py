from socket import *
port = 2_500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("", port))
sock.listen(1)

conn, (remotehost, remoteport) = sock.accept()
print("connected by", remotehost, remoteport)

while True:
    data = conn.recv(BUFSIZE)

    # TCP 연동이 강제적으로 끊겼을 경우
    if not data:
        break

    print("Received message: ", data.decode())
    conn.send(data)

conn.close()
sock.close()