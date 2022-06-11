"""
    간단한 웹 클라이언트: 텍스트 호출하기
    웹 클라이언트
"""

import requests


if __name__ == '__main__':
    url = "http://localhost:8080"
    rsp = requests.get(url)
    print(rsp.status_code)
    print(rsp.headers)
    print(rsp.text)