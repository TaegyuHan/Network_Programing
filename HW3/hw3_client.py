import socket

# 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9001) # 주소
sock.connect(addr) # 연결
msg = sock.recv(1024) # It is linked to the TCP calculator 메시지 받기
print(msg.decode())

while True:

    # 사용자로부터 게산식을 입력 받음
    calculation_formula = input("Please enter the calculation formula : ")

    sock.send(calculation_formula.encode())

    # 종료하기
    if calculation_formula == "q":
        break

    # 계산후 결과를 받음
    result = sock.recv(1024).decode()
    print("Result :", result)

sock.close() # 소켓 연결 끊기