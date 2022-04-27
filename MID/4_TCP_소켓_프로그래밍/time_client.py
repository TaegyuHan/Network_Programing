from socket import *

sock = socket(AF_INET, SOCK_STREAM) # 시간 소켓
sock.connect(("localhost", 9999)) # 주소 연동
print("Time: ", sock.recv(1024).decode()) # 데이터 받기
sock.close() # 소켓 연결 해제