from socket import *
import numpy as np
import cv2

BUF_SIZE = 8192
LENGTH = 10

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 5000))

while True:
    sock.send(b'start')

    rx_size = 0
    data = b""

    while rx_size < LENGTH:
        rx_buf = sock.recv(BUF_SIZE) # 이미지 받기
        if not rx_buf:
            break
        data += rx_buf
        rx_size += len(rx_buf)

    if rx_size < LENGTH:
        break

    frame_len = int(data)

    sock.send(b"image")

    rx_size = 0
    byte_data = b""
    while rx_size < frame_len: # 실제 이미지 수신
        rx_buf = sock.recv(BUF_SIZE)
        if not rx_buf:
            break

        byte_data += rx_buf
        rx_size += len(rx_buf)

    if rx_size < frame_len:
        break

    data = np.frombuffer(byte_data, dtype="uint8")
    img_decode = cv2.imdecode(data, 1)
    cv2.imshow("image", img_decode)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

sock.close()