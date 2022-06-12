"""
    카카오 API 사용하기: 번역 (문장 번역하기)
"""

import requests

API_URL = "https://dapi.kakao.com/v2/translation/translate"
REST_API_KEY = '토큰'


def translate_get(text: str) -> dict:
    """ 번역 GET 요청 """
    headers = {"Authorization": f"KakaoAK {REST_API_KEY}"}

    data = {
        "src_lang": "kr",
        "target_lang": "en",
        "query": text,
    }
    rsp = requests.get(API_URL, headers=headers, params=data)
    return rsp.json()


def translate_post(text: str) -> dict:
    """ 번역 POST 요청 """
    headers = {"Authorization": f"KakaoAK {REST_API_KEY}"}

    data = {
        "src_lang": "kr",
        "target_lang": "fr",
        "query": text,
    }
    rsp = requests.post(API_URL, headers=headers, params=data)
    return rsp.json()


if __name__ == '__main__':
    while True:
        text = input("Enter the sentence to translate: ")
        if text != "q":

            translated_text = translate_get(text)
            print(translated_text)
            print("[GET]", translated_text["translated_text"][0][0])

            translated_text = translate_post(text)
            print(translated_text)
            print("[POST]", translated_text["translated_text"][0][0], "\n")

        else:
            break