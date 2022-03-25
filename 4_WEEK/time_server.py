import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 9_999))
s.listen(5)

while True:
    client, addr = s.accept()
    print("connection from ", addr)
    # time.time()
    # UTC 기준 1970 1월 1일 0시 0분 0초 부터의 경과 시간을 나타냄

    # time.ctime()
    # 초 단위의 시간을 문자열로 변환하는 함수
    client.send(time.ctime(time.time()).encode())
    client.close()