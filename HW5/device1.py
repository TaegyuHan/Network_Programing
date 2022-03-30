import json
import random
from socket import *


class Device1:
    """
        사용자로부터 ‘Request’ 메시지를 수신하면 온도, 습도, 조도를 전송

        - 온도: 0~40 사이의 임의의 정수를 반환
        - 습도: 0~100 사이의 임의의 정수를 반환
        - 조도: 70~150 사이의 임의의 정수를 반환
    """

    IPV4 = ""
    PORT = 8001
    ADDRESS = (IPV4, PORT)
    BUFSIZE = 1_024

    def _get_data(self) -> str:
        """ 디바이스 데이터 얻기 """

        data = {
            "temperature": random.randint(0, 40), # 온도
            "humidity": random.randint(0, 100), # 습도
            "illumination": random.randint(0, 150) # 조도
        }

        return json.dumps(data)

    def run(self) -> None:
        """ 디바이스 실행 """
        print("Run device1!!")

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

                    # 잘못 요청
                    if data != "Request":
                        conn.close()
                        continue

                    # 정상 요청
                    data = self._get_data()
                    conn.send(data.encode())

                if server_break:
                    break


def main():
    D = Device1()
    D.run()


if __name__ == '__main__':
    main()