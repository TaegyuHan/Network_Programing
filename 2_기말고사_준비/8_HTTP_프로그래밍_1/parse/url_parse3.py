"""
    URL 결합하기
"""

from urllib import parse


# parse.urljoin 함수 사용
iot_url_1 = parse.urljoin("https://home.sch.ac.kr", "iot")
print("IoT Homepage 1:", iot_url_1)


# 문자열 더하기
iot_url_2 = "https://home.sch.ac.kr" + "iot"
print("IoT Homepage 1:", iot_url_2)


big_url = parse.urljoin("https://home.sch.ac.kr", "bigdata")
print("Bigdata Homepage:", big_url)

p_url = parse.urlparse(iot_url_1)
print("Parsed URL:", p_url)
print("Parsed URL:", p_url.geturl())


url = parse.urlunparse(p_url)
print("Encoded:", url)