"""
    웹에서 JSON 데이터 수신하기
"""

import json
from urllib import request


url = "http://python.bakyeono.net/data/movies.json"
text_data = request.urlopen(url).read().decode()
print(text_data)
print(type(text_data))


movies = json.loads(text_data)
sorted_by_year = sorted(movies,
                        key=lambda t:t["year"])

for moive in sorted_by_year:
    print(moive["year"],
          moive["title"],
          moive["genre"],
          moive["starring"])