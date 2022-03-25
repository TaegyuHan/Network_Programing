import socket

# 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9001) # 주소
sock.connect(addr) # 연결
msg = sock.recv(1024) # Hello 메시지 받기
print(msg.decode()) # Hello 메시지 출력

# 과제 코드
# 본인의 이름을 문자열로 전송
sock.send(b"Taegyu Han")

# 본인의 학번을 수신 후 출력
byte_student_number = sock.recv(1024)
print(int.from_bytes(bytes=byte_student_number, byteorder="big"))

sock.close() # 소켓 연결 끊기