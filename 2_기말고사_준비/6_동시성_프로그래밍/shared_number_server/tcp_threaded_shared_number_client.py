"""
    공유 자원을 사용하는 프로그램: 클라이언트

    Python 3.9 버전 이하에서만 경쟁상태 발생
"""

from socket import *

from oauthlib.uri_validate import port

PORT = 2500
BUF_SIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", port))

print(int(s.recv(BUF_SIZE).decode()))
s.close()