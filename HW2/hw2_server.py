import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # server 소켓 생성
s.bind(('', 9_001)) # IP, PORT 설정
s.listen(2)

# 학생 정보
student_information = {
    "Taegyu Han": 20171483
}

while True: # server 대기 시작
    client, addr = s.accept() # 클라이언트 소켓 정보
    print("Connection from ", addr) # 클라이언트 주소 출력
    client.send(b"Hello " + addr[0].encode()) # 클라이언트에게 클라이언트 주소 전송

    # 학생의 이름을 수신한 후 출력
    name = client.recv(1024)
    name = name.decode()
    print(name)

    # 학생의 학번을 전송
    try: # 존재 하는 학생
        student_number = student_information[name]
        byte_student_number = student_number.to_bytes(length=4, byteorder="big")
        client.send(byte_student_number)

    except KeyError as e: # 존재 하지 않는 학생
        client.send((404).to_bytes(length=4, byteorder="big"))

    client.close() # 클라이언트 소켓 연결 끊기