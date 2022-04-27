from socket import *

sock = socket(AF_INET, SOCK_STREAM) # 소켓 생성
addr = ("localhost", 9000) # 전송할 서버 선택
sock.connect(addr) # 소켓 연결
msg = sock.recv(1024) # 메시지 받기
print(msg.decode()) # 바이트 코드에서 문자열로 변경

sock.close() # 소켓 연결 끊기