"""
    kakao API 사용
"""
import PIL
from PIL import Image, ImageDraw
from io import BytesIO
import requests


API_URL = 'https://dapi.kakao.com/v2/vision/thumbnail/crop'
REST_API_KEY = '447145f6d9f94e5468fc93b5eaba9be6'


def detect_product(image_url: str, width: int, height: int) -> dict:
    """ 이미지 정보 API 호출 """
    headers = {"Authorization": f"KakaoAK {REST_API_KEY}"}
    data = {
        "image_url": image_url,
        "width": width,
        "height": height
    }
    resp = requests.post(API_URL, headers=headers, data=data)
    return resp.json()


def show_image(rep_json: dict):
    """ 이미지 보여주기 """
    url = rep_json["thumbnail_image_url"]
    image_rsp = requests.get(url)
    file_jpgdata = BytesIO(image_rsp.content)
    image = Image.open(file_jpgdata)
    image.show()


if __name__ == '__main__':
    IMAGE_URL = "https://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/07.jpg"
    width = input("width: ")
    height = input("height: ")
    detection_reult = detect_product(IMAGE_URL, width=width, height=height)
    show_image(detection_reult)
