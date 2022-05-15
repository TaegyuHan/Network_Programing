"""
    POST 사용하기
"""
import requests

url = "https://httpbin.org/post"
data = {"IoT": "2017"}
rsp = requests.post(url, data)
print(rsp.text)

rsp = requests.post(url, json=data)
print(rsp.text)

files = {"file": open("iot.jpg", "rb")}
rsp = requests.post(url, files=files)
print(rsp.text)