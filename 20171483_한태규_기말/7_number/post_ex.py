"""
    POST
"""

import requests

url = "https://httpbin.org/post"
data = {
    "ID": "20171483",
    "Name": "Han Tae-gyu",
    "Department": "IoT",
}

# POST 요청
req = requests.post(
    url=url,
    data=data
)
print(req.text)

# 반환 데이터
json_data = req.json()
print(json_data["form"])
