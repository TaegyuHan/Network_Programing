"""
    delete, head 사용하기
"""
import requests

rsp = requests.delete("https://httpbin.org/delete")
print(rsp.text)

rsp = requests.get("https://httpbin.org/get")
print(rsp.headers)
print(rsp.text)