from socket import *
from collections import deque


class Request:
    BAD = 400
    SEND = "send"
    RECEIVE = "receive"
    EXIT = "quit"


class Response:
    NO_MESSAGES = "No messages"


class Server:
    """
        1. 클라이언트로부터 “send [mboxID] message” 메시지 수신 시, 해당 [mboxID]에
           message를 저장하고, “OK”를 클라이언트로 전송

            - [mboxID]는 숫자, 문자 모두 가능
            - message는 여러 단어로 구성될 수 있음

        2. 클라이언트로부터 “receive [mboxID]” 메시지 수신 시, 해당 [mboxID]의 제일 앞에
           있는 메시지를 클라이언트로 전송한 후 삭제

            - 존재하지 않는 [mboxID]나 메시지가 없는 [mboxID]에 대해 “receive [mboxID]”를
              수신하는 경우 “No messages”를 클라이언트로 전송

        3. 클라이언트로부터 “quit” 메시지 수신 시, 프로그램 종료
    """

    IPv4 = ""
    PORT = 3333
    ADDRESS = (IPv4, PORT)
    BUFF_SIZE = 1_024

    def __init__(self):
        """ 메시지 저장 """
        self.data = {}

    def _data_parsing(self, data: str) -> (int, str, str) or \
                                          (str, str, str):
        """ 메시지 데이터 파싱

        :param data: 클라이언트에서 받은 데이터

        :return:
            실패 케이스 : (int, str, str)
                state : BAD (400) 실패 코드

            성공 케이스 : (str, str, str)

                state : 상태
                    - SEND : 데이터 저장
                    - RECEIVE : 데이터 찾기
                    - EXIT : 종료
                mboxID : 메시지 박스 아이디
                msg : 메시지 내용

        """
        # 종료 요청
        if data == Request.EXIT:
            return Request.EXIT, "", ""

        data = data.split()
        try:
            state, mboxID, msg = data[0], data[1], " ".join(data[2:])
        except IndexError: # 인덱스 파싱 실패
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

    def _insert_data(self, id: str, msg: str) -> None:
        """ 메시지 받기

        :param id: 메시지 박스 아이디
        :param msg: 메시지 내용

        :return: None
        """

        # 기존의 id 존재 안함
        if id not in self.data.keys():
            self.data[id] = deque([msg])
            return

        # 기존의 id 존재
        self.data[id].append(msg)
        return

    def _select_data(self, id: str) -> str:
        """ 메시지 주기

        :param id: 메시지 박스 아이디

        :return: 응답 메시지 내용
        """

        # 기존의 id 존재 안함
        if id not in self.data.keys():
            return Response.NO_MESSAGES

        # 데이터 가져오기
        try:
            data = self.data[id].popleft()
        except IndexError: # 큐에 데이터 없음
            del self.data[id] # 큐 삭제
            return Response.NO_MESSAGES

        # 데이터 찾기 성공
        return data

    def run(self) -> None:
        """ 서버 실행 """
        print("Run server!")

        # 서버 소켓 생성
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.bind(("", self.PORT))

        while True:
            client_data, addr = sock.recvfrom(self.BUFF_SIZE)
            data = client_data.decode()

            # 데이터 파싱
            state, mboxID, msg = self._data_parsing(data)

            # 종료 요청
            if state == Request.EXIT:
                sock.close()
                break

            # 잘못된 요청
            if state == Request.BAD:
                sock.sendto(b"400 Bad Request", addr)

            print(addr, state, mboxID, msg)

            # send 요청
            if state == Request.SEND:
                # 데이터 넣기
                self._insert_data(id=mboxID, msg=msg)
                sock.sendto(b"OK", addr)

            # receive 요청
            elif state == Request.RECEIVE:
                # 데이터 불러오기
                response_data = self._select_data(id=mboxID)
                sock.sendto(response_data.encode(), addr)


def main() -> None:
    S = Server()
    S.run()


if __name__ == '__main__':
    main()