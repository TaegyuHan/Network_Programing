"""
    requests 모듈: GET
"""

import requests
from aiohttp import payload

rsp = requests.get("https://naver.com")
print(rsp.status_code)  # 응답 상태 코드
print(rsp.encoding)  # 응답 데이터의 인코딩

url = "https://search.naver.com/search.naver"
payload = {"query": "IoT"}
rsp = requests.get(url, params=payload)
print(rsp.url)
print(rsp.headers)
print(rsp.text[:1000])