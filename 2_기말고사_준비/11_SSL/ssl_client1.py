"""
    SSL 클라이언트 예제
"""
import ssl
import socket

host_name = "home.sch.ac.kr"

context = ssl.create_default_context()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = context.wrap_socket(sock, server_hostname=host_name)
conn.connect((host_name, 443))

conn.send(b"HEAD /sch/index.jsp HTTP/1.0\r\nHost: home.sch.ac.kr\r\n\r\n")

msg = conn.recv(4096)
print(msg.decode())