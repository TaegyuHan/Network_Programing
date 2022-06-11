"""
    HTTP Request 전송
"""

from urllib import request

rsp = request.urlopen("https://home.sch.ac.kr/iot")
print("HTTP Response: ", rsp)
print("URL:", rsp.geturl())  # URL
print("Status:", rsp.getcode())  # states code

headers = rsp.info()
print("Date:", headers["date"])  # Date: Sat, 11 Jun 2022 15:36:20 GMT
print("Headers")
print("------------")
print(headers)

data = rsp.read().decode()
print("Length:", len(data))
print("Data")
print("------------")
print(data)
