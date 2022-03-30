import random
from socket import *


class Server:
    """
        고려 사항

        수신 측
            − 50%의 확률로 ‘ack’을 보내지 않음 (고의로 50%의 데이터 손실을 만듬)
            − ‘ack’ 전송 후, 채팅 메시지를 화면에 출력

        송신 측
            - 재전송 횟수가 3번 이하인 경우, 메시지 전송
            - 타임아웃 시간을 2초로 설정하고, ‘ack’ 응답을 기다림
            - 타임아웃이 발생할 경우, 재전송 횟수를 1 증가시키고, 재전송
    """

    IPV4 = ""
    PORT = 3334
    ADDRESS = (IPV4, PORT)
    BUF_SIZE = 1_024

    def run(self) -> None:
        """ 서버 실행 """
        
        # 서버 소켓 생성
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.bind(('', self.PORT))

        while True:
            sock.settimeout(None)  # 소켓의 블로킹 모드 timeout 설정

            while True:  # None인 경우, 무한정 블로킹됨
                data, addr = sock.recvfrom(self.BUF_SIZE)

                if random.random() <= 0.5:
                    continue
                else:
                    sock.sendto(b'ack', addr)
                    print('<-', data.decode())
                    break

            msg = input("-> ")
            reTx = 0
            while reTx <= 3:
                resp = f"{str(reTx)} {msg}"
                sock.sendto(resp.encode(), addr)
                sock.settimeout(2)
                # 소켓의 timeout 설정. 해당 timeout 내 메시지
                # 수신을 못하면 timeout 예외 발생

                try:
                    data, addr = sock.recvfrom(self.BUF_SIZE)
                except timeout:
                    reTx += 1
                    continue
                else:
                    break

            # 3번이상 전송 실패시 종료
            if reTx > 3:
                break

        sock.close()

def main():
    S = Server()
    S.run()


if __name__ == '__main__':
    main()