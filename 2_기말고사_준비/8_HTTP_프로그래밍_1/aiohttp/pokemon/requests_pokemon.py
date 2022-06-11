"""
    aiohttp 모듈: 클라이언트 (동기)
"""

import requests
import time

if __name__ == '__main__':
    start_time = time.time()

    for number in range(1, 11):
        url = f"https://pokeapi.co/api/v2/pokemon/{number}"
        resp = requests.get(url)
        pokemon = resp.json()
        print(pokemon["name"])

    end_time = time.time()

    print(f"--- {end_time - start_time} seconds ---")