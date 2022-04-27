from socket import *

# SOCK_STREAM : TCP
# IPv4 : AF_INET

s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 9000)) # 자신의 서버 이름 ("ip", 포트번호)
s.listen(2) # backlog : 한번에 받을 소켓

while True:
    client, addr = s.accept() # 클라이언트 대기
    print("Connection from ", addr)
    client.send(b"Hello " + addr[0].encode()) # < 인터넷 세상에서는 bit로 전송해야 한다.
    client.close() # 클라이언트 소켓 닫기