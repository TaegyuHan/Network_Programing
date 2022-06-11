"""
    URL 파싱하기
"""
from urllib import parse


url = 'https://home.sch.ac.kr/sch/06/090000.jsp?mode=view&article_no=20220421103054467019&board_wrapper=%2Fsch%2F06%2F090000.jsp&pager.offset=0&board_no=20200302132057325672'

parsed_url = parse.urlsplit(url)

print(parsed_url)
# SplitResult(scheme='https', netloc='home.sch.ac.kr', path='/sch/06/090000.jsp', query='mode=view&article_no=20220421103054467019&board_wrapper=%2Fsch%2F06%2F090000.jsp&pager.offset=0&board_no=20200302132057325672', fragment='')

print('scheme :', parsed_url.scheme)
# scheme : https

print('netloc :', parsed_url.netloc)
# netloc : home.sch.ac.kr

print('path :', parsed_url.path)
# path : /sch/06/090000.jsp

print('query :', parsed_url.query)
# query : mode=view&article_no=20220421103054467019&board_wrapper=%2Fsch%2F06%2F090000.jsp&pager.offset=0&board_no=20200302132057325672

print('fragment:', parsed_url.fragment)
# fragment: