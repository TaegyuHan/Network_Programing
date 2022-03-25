import socket


port = int(input("Port No: "))
address = ("localhost", port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Message to send: ")
    try:
        bytes_send = s.send(msg.encode())

    except:
        print("connection closed")
        break
    else:
        print(f"{bytes_send} bytes send")

    try:
        data = s.recv(BUFSIZE)
    except:
        print("connection closed")
        break
    else:
        if not data:
            break
        print(f"Received message: {data.decode()}")

s.close()