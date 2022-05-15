"""
 URL 파싱하기
"""
from urllib import parse

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=iot"
parse_url = parse.urlparse(url)
print(parse_url)
print("scheme: ", parse_url.scheme)
print("netloc: ", parse_url.netloc)
print("path: ", parse_url.path)
print("params: ", parse_url.params)
print("query: ", parse_url.query)
print("fragment: ", parse_url.fragment)