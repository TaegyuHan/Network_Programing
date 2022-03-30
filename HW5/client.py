import json
from socket import *
from datetime import datetime


class User:
    """
        디바이스 사용자
        - 1 입력 > Device1 데이터 수신
        - 2 입력 > Device2 데이터 수신
        - quit 메시지를 종료 !
    """

    BUFSIZE = 1_024
    DEVICE_1 = "1"
    DEVICE_2 = "2"
    QUIT = "quit"
    SAVE_FILE_NAME = "data.txt"
    WEEKDAY = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    MONTH = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
             'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    def __init__(self):
        self.data = []

    def _device_connect(self, number: str) -> socket:
        """ 디바이스 연동 """

        # 1번 디바이스
        if number == self.DEVICE_1:
            HOST = "localhost"
            PORT = 8001

        # 2번 디바이스
        elif number == self.DEVICE_2:
            HOST = "localhost"
            PORT = 8002

        s = socket(AF_INET, SOCK_STREAM)
        s.connect((HOST, PORT))
        return s

    def _save_file(self) -> None:
        """ 받은데이터 파일에 저장 """

        with open(f"./{self.SAVE_FILE_NAME}", 'w') as writer:
            for row in self.data:
                write_line = (
                    f"{self.WEEKDAY[row['date_time'].weekday()]} "
                    f"{self.MONTH[row['date_time'].month]} "
                    f"{row['date_time'].strftime('%d %H:%M:%S %Y')}: "
                    f"Device{row['device']}: "
                )

                if row['device'] == self.DEVICE_1:
                    write_line += (
                        f"Temp={row['data']['temperature']}, "
                        f"Humid={row['data']['humidity']}, "
                        f"Iilum={row['data']['illumination']}\n"
                    )

                elif row['device'] == self.DEVICE_2:
                    write_line += (
                        f"Heartbeat={row['data']['heart_rate']}, "
                        f"Steps={row['data']['calories_burned']}, "
                        f"Cal={row['data']['calories_burned']}\n"
                    )

                writer.write(write_line)

        print(f"save file : {self.SAVE_FILE_NAME}")

    def run(self) -> None:
        """ 사용자 디바이스 연결 """

        # 소켓 TCP 연결
        device1, device2 = self._device_connect("1"), self._device_connect("2")

        while True:

            control_device = \
                input("Please enter the device number you want to use. (1 or 2) : ")
            
            # 원하는 input만 필터링
            if control_device not in (self.QUIT,
                                  self.DEVICE_1,
                                  self.DEVICE_2):

                print("Invalid input.")
                continue

            # 데이터 수신 끝
            if control_device == self.QUIT:
                device1.send(b"quit")
                device2.send(b"quit")
                device1.close()
                device2.close()
                self._save_file() # 데이터 저장
                break

            # device1 데이터 가져오기
            if control_device == self.DEVICE_1:
                device1.send(b"Request")
                tmp_data = device1.recv(self.BUFSIZE).decode()

            # device2 데이터 가져오기
            elif control_device == self.DEVICE_2:
                device2.send(b"Request")
                tmp_data = device2.recv(self.BUFSIZE).decode()

            # json data 읽기
            self.data.append({
                "date_time": datetime.now(),
                "data": json.loads(tmp_data),
                "device": control_device
            })


def main():
    D = User()
    D.run()


if __name__ == '__main__':
    main()