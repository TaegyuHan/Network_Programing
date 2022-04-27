from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM) # 서버 소켓 생성
sock.bind(("", port)) # 서버 소켓 생성
sock.listen(1) # 클라이언트 1개 받기

conn, (remotehost, remoteport) = sock.accept() # 대기
print("connected by ", remotehost, remoteport) # 주소 호출

while True: # 실행

    try: # 예외 처리
        data = conn.recv(BUFSIZE) # 데이터 받기
    except:
        break
    else:
        if not data: # 데이터가 없을시 멈춤
            break

        # 데이터 프린트 하기
        print("Received message: ", data.decode())

    try:
        conn.send(data)
    except:
        break

conn.close() # 소켓 닫기