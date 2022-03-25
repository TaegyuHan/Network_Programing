import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("localhost", 9999))
print("Time: ", socket.recv(1024).decode())
socket.close()