import json
from socket import *
from datetime import datetime

class Server:
    HOST = "localhost"
    PORT = 7777

class Input:
    """ 데이터 타입 """
    TYPE_1 = 1
    TYPE_2 = 1
    TYPE_3 = 1
    QUIT = "quit"

class Client:
    """
        디바이스 사용자
        - 1 입력 > Device1 데이터 수신
        - 2 입력 > Device2 데이터 수신
        - quit 메시지를 종료 !
    """
    BUFSIZE = 1_024

    def __init__(self):
        self.data = []

    def _data_split(self, data):
        """ 받은 바이트 데이터 나누기 """
        temperature = int.from_bytes(data[:4], "big")
        humidity = int.from_bytes(data[4:8], "big")
        illumination = int.from_bytes(data[8:], "big")
        return temperature, humidity, illumination

    def run(self):
        """ 소켓 연결 """
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((Server.HOST, Server.PORT))

        while True:
            data_type = input("원하는 데이터 타입을 입력해주세요!: ")

            # 원하는 데이터 필터링
            if data_type not in ["1", "2", "3"]:
                print("데이터를 잘못 입력했습니다.")
                continue

            # 데이터 전송
            s.send(data_type.encode())

            # 데이터 받기
            data = s.recv(self.BUFSIZE)

            temperature, humidity, illumination = self._data_split(data)
            print(f"Temp={temperature}, Humid={humidity}, Lumi={illumination}")


def main():
    D = Client()
    D.run()


if __name__ == '__main__':
    main()