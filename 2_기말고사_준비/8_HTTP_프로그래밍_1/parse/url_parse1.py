"""
    urllib.parse 모듈: urlparse()

    URL 파싱하기
"""

from urllib import parse

if __name__ == '__main__':
    url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=iot"

    parsed_url = parse.urlparse(url)
    print(parsed_url)  # 전부 출력
    #  ParseResult(scheme='https', netloc='search.daum.net', path='/search', params='', query='w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=iot', fragment='')

    print("scheme :", parsed_url.scheme)
    # scheme : https

    print("netloc :", parsed_url.netloc)
    # netloc : search.daum.net

    print("path :", parsed_url.path)
    # path : /search

    print("params :", parsed_url.params)
    # params :

    print("query :", parsed_url.query)
    # query : w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=iot

    print("fragment :", parsed_url.fragment)
    # fragment :