from socket import *


class Request:
    EXIT = "quit"


class Client:
    """
        1. 사용자로부터 “send [mboxID] message” 또는 “receive [mboxID]” 또는 “quit”
           문자열을 입력받음

        2. 입력받은 문자열을 서버로 전송
            − “quit” 문자열 전송 후, 프로그램 종료

        3. 응답으로 받은 문자열을 화면에 출력
    """

    SERVER_IPv4 = "localhost"
    PORT = 3333
    ADDRESS = (SERVER_IPv4, PORT)
    BUFF_SIZE = 1_024
    INPUT_MESSAGE = (
        'Enter the message("send mboxId message" or "receive mboxId"):'
    )

    def run(self):
        """ 클라이언트 실행 """

        sock = socket(AF_INET, SOCK_DGRAM)

        while True:
            data = input(Client.INPUT_MESSAGE)
            sock.sendto(data.encode(), self.ADDRESS)

            # 클라이언트 종료
            if data == Request.EXIT:
                break

            data, addr = sock.recvfrom(self.BUFF_SIZE)
            print(data.decode())

        sock.close()


def main():
    C = Client()
    C.run()


if __name__ == '__main__':
    main()