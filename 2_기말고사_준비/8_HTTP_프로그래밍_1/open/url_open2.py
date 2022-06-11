"""
    HTTP를 통한 (폼) 데이터 전송

    이 코드는 단독으로
    동작하지 않음
    (응답할 웹서버가 필요함)
"""

from urllib import parse, request

query = {
    "temperature": "25",
    "humidity": "60"
}
encoded_query = parse.urlencode(query)  # temperature=25&humidity=60
url = "http://localhost:8080/"
get_url = f"{url}?{encoded_query}"  # http://localhost:8080/?temperature=25&humidity=60

# 서버가 필요함
# # GET
# rsp = request.urlopen(get_url)
# print(rsp.read().decode())
#
# # POST
# rsp = request.urlopen(url, encoded_query.encode())