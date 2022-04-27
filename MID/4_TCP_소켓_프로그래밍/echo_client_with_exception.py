from socket import *

port = int(input("Port No: ")) # 포트번호 입력
address = ("localhost", port) # 주소 입력
BUFSIZE = 1024 # 버퍼 사이즈

s = socket(AF_INET, SOCK_STREAM) # 소켓 생성
s.connect(address) # 연결

while True:
    msg = input("Message to send: ") # 전송할 메시지 받기

    try:
        # 메시지 전송
        bytes_send = s.send(msg.encode())
    except:
        print("connection closed")
    else:
        print(f"{bytes_send} bytes send")

    try:
        # 데이터 받기
        data = s.recv(BUFSIZE)
    except:
        print("connection closed")
        break
    else:

        if not data:
            # 데이터 없을시 멈춤
            break
            
        # 받은 데이터 출력
        print(f"Received message: {data.decode()}")

s.close()