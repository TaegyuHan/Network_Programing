import json
import random
from socket import *

class Data:
    TYPE_1 = "1"
    TYPE_2 = "2"
    TYPE_3 = "3"

class Server:
    """
        사용자로부터 ‘Request’ 메시지를 수신하면 온도, 습도, 조도를 전송

        - 온도: 1~50 사이의 임의의 정수를 반환
        - 습도: 1~100 사이의 임의의 정수를 반환
        - 조도: 1~150 사이의 임의의 정수를 반환
    """

    IPV4 = ""
    PORT = 7777
    ADDRESS = (IPV4, PORT)
    BUFSIZE = 1_024

    def _get_data(self, type) -> str:
        """ server 데이터 얻기 """

        zero = 0
        data = {
            "temperature": random.randint(1, 50), # 온도
            "humidity": random.randint(1, 100), # 습도
            "illumination": random.randint(1, 150) # 조도
        }

        # 바이트 코드 반환
        if type == Data.TYPE_1:
            return data["temperature"].to_bytes(4, "big")\
                   + (zero.to_bytes(4, "big") * 2)
        elif type == Data.TYPE_2:
            return zero.to_bytes(4, "big")\
                   + data["humidity"].to_bytes(4, "big")\
                   + zero.to_bytes(4, "big")
        elif type == Data.TYPE_3:
            return (zero.to_bytes(4, "big") * 2)\
                   + data["illumination"].to_bytes(4, "big")

    def run(self) -> None:
        """ 온도, 습도, 조도 서버 실행 """
        print("Run Server!!")

        with create_server(self.ADDRESS) as server:
            server_break = False

            while True:
                conn, addr = server.accept()

                while True:
                    # 사용자에게 Request 받기
                    data = conn.recv(self.BUFSIZE).decode()

                    # 디바이스 종료
                    if data == "quit" or not data:
                        server_break = True
                        break

                    # 정상 요청
                    data = self._get_data(data)
                    conn.send(data)

                if server_break:
                    break


def main():
    D = Server()
    D.run()


if __name__ == '__main__':
    main()