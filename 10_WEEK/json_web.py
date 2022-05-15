"""
    웹에서 json 데이터 수신하기
"""
import json
from urllib import request

url = 'https://python.bakyeono.net/data/movies.json'

text_data = request.urlopen(url).read().decode()
print(text_data)
print(type(text_data))

movies = json.loads(text_data)
sorted_by_year = sorted(movies,
                        key=lambda t: t["year"])
for movie in sorted_by_year:
    print(movie["year"],
          movie["title"],
          movie["genre"],
          movie["starring"])