import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # server 소켓 생성
s.bind(('', 9_001)) # IP, PORT 설정
s.listen(2)
client, addr = s.accept()  # 클라이언트 소켓 정보
print("Connection from ", addr)  # 클라이언트 주소 출력
client.send(b"It is linked to the TCP calculator." + addr[0].encode())  # 클라이언트에게 클라이언트 주소 전송

while True: # server 대기 시작

    # calculation formula
    data = client.recv(1024)

    # 클라이언트 쪽에서 통신이 끊겼을 경우
    if not data:
        break

    calculation_formula = data.decode()
    print("anser to > ", addr)

    # 종료하기
    if calculation_formula == "q":
        break

    try:
        # 결과 계산
        answer = eval(calculation_formula)

        if isinstance(answer, int): # 결과가 정수인 경우
            client.send(str(answer).encode())

        elif isinstance(answer, float): # 결과가 실수인 경우 (소수점 1자리까지 표시)
            client.send(str(round(answer, 1)).encode())

    except ZeroDivisionError: # 0을 나누는 경우
        client.send(b"Zero is indivisible.")

    except Exception as e: # 식을 정확하게 안받은 경우
        client.send(b"Please enter the calculation formula correctly.")

client.close() # 클라이언트 소켓 연결 끊기
s.close()