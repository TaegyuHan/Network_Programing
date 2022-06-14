"""
    URL 파싱하기
"""
from urllib import parse
import requests

url = "https://search.naver.com/search.naver?query=iot"


# A
parsed_url = parse.urlparse(url)
print(parsed_url)  # 전부 출력

# B
new_url = (
    f"{parsed_url.scheme}://"
    f"{parsed_url.netloc}"
    f"{parsed_url.path}"
)
print(new_url)


# C
query = input("input qnuery: ")
search_url = f"{new_url}?query={query}"

# D
rep = requests.get(search_url)
print(rep.headers)