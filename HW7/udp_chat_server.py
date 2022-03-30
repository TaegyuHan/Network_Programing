import json
import random
from socket import *


class Server:
    """
        고려 사항
        - 채팅 메시지가 전송 도중에 손실될 수 있음
        - 채팅 메시지가 잘 전송되었는지 알기 위해, 수신 측에서는 ‘ack’ 메시지를 전송

        수신 측
        − 50%의 확률로 ‘ack’을 보내지 않음 (고의로 50%의 데이터 손실을 만듬)
        − ‘ack’ 전송 후, 채팅 메시지를 화면에 출력
    """

    IPV4 = ""
    PORT = 3333
    ADDRESS = (IPV4, PORT)
    BUFSIZE = 1_024

    def run(self) -> None:
        """ 서버 실행 """
        print("Run server")
        
        # 서버 소켓 생성
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.bind(('', self.PORT))

        while True:
            sock.settimeout(None)  # 소켓의 블로킹 모드 timeout 설정

            while True:  # None인 경우, 무한정 블로킹됨
                data, addr = sock.recvfrom(self.BUFF_SIZE)

                if random.random() <= 0.5:
                    continue
                else:
                    sock.sendto(b'ack', addr)
                    print('<-', data.decode())
                    break


def main():
    S = Server()
    S.run()


if __name__ == '__main__':
    main()