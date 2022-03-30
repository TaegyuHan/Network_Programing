from socket import *
import cv2
import numpy as np

BUF_SIZE = 8192
LENGTH = 10
video_file = "./test.mp4"
socket = socket(AF_INET, SOCK_STREAM)
socket.bind(("", 5000))
socket.listen(5)

while True:
    csock, addr = socket.accept()
    print("Client is connected")
    cap = cv2.VideoCapture(video_file)

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            temp = csock.recv(BUF_SIZE) # start 받기
            if not temp:
                break

            result, img_encode = cv2.imencode(".jpg", frame)
            data = np.array(img_encode)
            byte_data = data.tobytes()
            csock.send(str(len(byte_data)).zfill(LENGTH).encode())

            temp = csock.recv(BUF_SIZE)
            if not temp:
                break

            csock.send(byte_data)

        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    csock.close()