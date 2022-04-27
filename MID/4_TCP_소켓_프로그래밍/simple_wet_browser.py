from socket import *

sock = socket(AF_INET, SOCK_STREAM) # 소켓 생성
sock.connect(("google.com", 80)) # 구글과 연결
sock.send(b"GET / HTTP/1.1\r\n\r\n") # GET 요청
data = sock.recv(1000) # 데이터 받기
print(data.decode()) # 데이터 전환
sock.close() # 소켓 연결 끊기

