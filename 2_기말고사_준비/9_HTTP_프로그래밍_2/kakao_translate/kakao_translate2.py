"""
    카카오 API 사용하기: 번역 (언어 감지하기)
"""

import requests

API_URL_1 = "https://dapi.kakao.com/v2/translation/translate"
API_URL_2 = "https://dapi.kakao.com/v3/translation/language/detect"
REST_API_KEY = '토큰'

def detect_language_get(text: str) -> dict:
    """ 언어 감지 GET 메소드 """
    headers = {"Authorization": f"KakaoAK {REST_API_KEY}"}

    data = {"query": text}
    rsp = requests.get(API_URL_2, headers=headers, params=data)
    return rsp.json()


def translate_post(text: str, src_lang: str) -> dict:
    """ 번역 POST 요청 """
    headers = {"Authorization": f"KakaoAK {REST_API_KEY}"}

    data = {
        "src_lang": src_lang,
        "target_lang": "jp",
        "query": text,
    }
    rsp = requests.post(API_URL_1, headers=headers, params=data)
    return rsp.json()


if __name__ == '__main__':
    while True:
        text = input("Enter the sentence to translate: ")

        if text != "q":
            detect_output = detect_language_get(text)
            print(detect_output)

            detect_lang = detect_output["language_info"][0]["code"]
            translated_text = translate_post(text, detect_lang)
            print(translated_text)

            print("[POST],", translated_text["translated_text"][0][0], "\n")

        else:
            break