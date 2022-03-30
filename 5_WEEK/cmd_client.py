from socket import *
import argparse


BUFSIZE = 1024
# 소켓
s = socket(AF_INET,SOCK_STREAM)

parser = argparse.ArgumentParser()
parser.add_argument("-s", default="localhost")
parser.add_argument("-p", type=int, default=2500)

agrs = parser.parse_args()
s.connect((agrs.s, agrs.p))
print("connected to ", agrs.s, agrs.p)

while True:
    msg = input("Message to send: ")
    if msg == 'q': # 종료버튼
        break
    print(f"send : {s.send(msg.encode())}")
    data = s.recv(BUFSIZE)
    if not data:
        break
    print("Received message: ", data.decode())

s.close()


