from select import *
from socket import *
from collections import deque

socks = []
BUFFER = 1024
PORT = 2550

s_sock = socket()
s_sock.bind(("", PORT))
s_sock.listen()

socks.append(s_sock)
print(f"{str(PORT)}에서 접속 대기중")


class D:
    DATA = {}

class Request:
    BAD = 400
    SEND = "send"
    RECEIVE = "receive"
    EXIT = "quit"

class Response:
    NO_MESSAGES = "No messages"

def data_parsing(recv_data):
    """ 데이터 파싱 """
    # 종료 요청
    if recv_data == Request.EXIT:
        return Request.EXIT, "", ""

    data = recv_data.split()

    try:
        state, mboxID, msg = data[0], data[1], " ".join(data[2:])
    except IndexError:  # 인덱스 파싱 실패
        return Request.BAD, "", ""

    # 잘못된 요청 ( 전송 문자 )
    if state not in (Request.SEND, Request.RECEIVE):
        return Request.BAD, "", ""

    # 잘못된 요청 ( 전송 문자 )
    if state == Request.SEND and msg == "":
        return Request.BAD, "", ""

    # 잘못된 요청 ( ID 정보 )
    if not mboxID.isdigit():
        return Request.BAD, "", ""

    # 성공
    return state, mboxID, msg

def insert_data(id: str, msg: str) -> None:

    # 기존의 id 존재 안함
    if id not in D.DATA.keys():
        D.DATA[id] = deque([msg])
        return

    # 기존의 id 존재
    D.DATA[id].append(msg)
    return

def select_data(id: str) -> str:
    """ 메시지 주기

    :param id: 메시지 박스 아이디

    :return: 응답 메시지 내용
    """

    # 기존의 id 존재 안함
    if id not in D.DATA.keys():
        return Response.NO_MESSAGES

    # 데이터 가져오기
    try:
        data = D.DATA[id].popleft()
    except IndexError: # 큐에 데이터 없음
        del D.DATA[id] # 큐 삭제
        return Response.NO_MESSAGES

    # 데이터 찾기 성공
    return data


while True:
    r_sock, w_sock, e_sock = select(socks, [], [])
    for s in r_sock:
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print(f"Client ({addr}) connected")

        else:
            data = s.recv(BUFFER)
            if not data:
                s.close()
                socks.remove(s)
                continue

            state, mboxID, msg = data_parsing(data.decode())

            # 종료 요청
            if state == Request.EXIT:
                s.close()
                socks.remove(s)
                continue

            # 잘못된 요청
            if state == Request.BAD:
                s.send(b"400 Bad Request")

            # send 요청
            if state == Request.SEND:
                # 데이터 넣기
                insert_data(id=mboxID, msg=msg)
                s.send(b"OK")

            # receive 요청
            elif state == Request.RECEIVE:
                # 데이터 불러오기
                response_data = select_data(id=mboxID)
                s.send(response_data.encode())

            print(state, mboxID, msg)
            print(D.DATA)