"""
 URL 파싱하기
"""
from urllib import parse

url = "https://home.sch.ac.kr/sch/06/090000.jsp?mode=view&article_no=20220421103054467019&board_wrapper=%2Fsch%2F06%2F090000.jsp&pager.offset=0&board_no=20200302132057325672"
parse_url = parse.urlparse(url)
print(parse_url)
print("scheme: ", parse_url.scheme)
print("netloc: ", parse_url.netloc)
print("path: ", parse_url.path)
print("params: ", parse_url.params)
print("query: ", parse_url.query)
print("fragment: ", parse_url.fragment)