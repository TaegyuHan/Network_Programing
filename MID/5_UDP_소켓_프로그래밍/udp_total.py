import argparse, socket, random
from datetime import datetime
BUFF_SIZE = 1024

def Server(ipaddr, port): # 서버 함수
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipaddr, port))
    print('Waiting in {}...'.format(sock.getsockname()))
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() < prob:
            print('Message from {} is lost.'.format(addr))
            continue
        print('{} client message {!r}'.format(addr, data.decode()))
        text = 'The length is {} bytes.'.format(len(data))
        sock.sendto(text.encode(), addr)

def Client(hostname, port): # 클라이언트 함수
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    index = 1 # 보낸 메시지 번호
    time = 0.1 # seconds
    while True:
        data = str(datetime.now())
        sock.sendto(data.encode(), (hostname, port))
        print('({}) Waiting for {} sec'.format(index, time))
        sock.settimeout(time)

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except socket.timeout:
            time *= 2
            if time > 2.0:
                print('{}th packet is lost'.format(index))
                if index >= sending_counts:
                    break
                index += 1
                time = 0.1
        else:
            print('Server reply: {!r}'.format(data.decode()))
        if index >= sending_counts:
            break
        index += 1
        time = 0.1