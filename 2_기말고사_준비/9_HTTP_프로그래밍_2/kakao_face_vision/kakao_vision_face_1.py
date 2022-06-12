"""
    카카오 API 사용하기: 비전 (얼굴 검출)
"""

import requests

API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
REST_API_KEY = '토큰'

# api_key와 이미지 파일을 POST로 전송하여 얼굴 검출을 수행
headers = {"Authorization": f"KakaoAK {REST_API_KEY}"}
files = {"image": open("test_image.jpg", "rb")}
rsp = requests.post(API_URL, headers=headers, files=files)
print(rsp.json())