import json
import random
from socket import *


class Device2:
    """
        온도, 습도, 조도 전송 방법은 자유롭게 선택

        - 심박수: 40~140 사이의 임의의 정수를 반환
        - 걸음수: 2000~6000 사이의 임의의 정수를 반환
        - 조소모칼로리: 1000~4000 사이의 임의의 정수를 반환
    """

    IPV4 = ""
    PORT = 8002
    ADDRESS = (IPV4, PORT)
    BUFSIZE = 1_024

    def _get_data(self) -> str:
        """ 디바이스 데이터 얻기 """

        data = {
            "heart_rate": random.randint(40, 140), # 온도
            "steps": random.randint(2_000, 6_000), # 습도
            "calories_burned": random.randint(1_000, 4_000) # 조도
        }

        return json.dumps(data)

    def run(self) -> None:
        """ 디바이스 실행 """
        print("Run device2!!")

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
    D = Device2()
    D.run()


if __name__ == '__main__':
    main()