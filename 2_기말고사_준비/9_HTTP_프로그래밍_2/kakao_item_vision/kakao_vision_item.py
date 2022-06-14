"""
    카카오 API 사용하기: 비전 (상품 검출)
"""
import PIL.JpegImagePlugin
import requests
from PIL import Image, ImageDraw
from io import BytesIO

from HW10.kakao_login import REST_API_KEY

API_URL = "https://dapi.kakao.com/v2/vision/product/detect"
REST_API_KEY = '토큰'


def detect_product(image_url: str) -> dict:
    """ 이미지 정보 API 호출 """
    headers = {"Authorization": f"KakaoAK {REST_API_KEY}"}
    data = {"image_url": image_url}
    resp = requests.post(API_URL, headers=headers, data=data)
    return resp.json()


def show_products(image_url: str, detection_reult: dict) -> PIL.JpegImagePlugin.JpegImageFile:
    """ 상품 결과를 이미지에 표시하는 함수 """
    image_rsp = requests.get(image_url)  # 이미지 다운로드
    file_jpgdata = BytesIO(image_rsp.content)

    image = Image.open(file_jpgdata)

    draw = ImageDraw.Draw(image)
    for item in detection_reult["result"]["objects"]:
        x1 = int(item["x1"] * image.width)
        y1 = int(item["y1"] * image.height)
        x2 = int(item["x2"] * image.width)
        y2 = int(item["y2"] * image.height)

        # 검출 위치에 사각형 그리기
        draw.rectangle([(x1, y1), (x2, y2)], fill=None, outline='red', width=2)
        draw.text((x1 + 5, y1 + 5), item["class"], (0, 0, 0))  # 상품 이름 그리기

    del draw

    return image

if __name__ == '__main__':
    # 상품 검출할 이미지의 URL
    IMAGE_URL = "https://w7.pngwing.com/pngs/632/327/png-transparent-man-wearing-white-t-shirt-riding-bicycle-bicycle-pedal-architecture-manhattan-brooklyn-cycling-texture-bicycle-frame-bicycle.png"
    # IMAGE_URL = "https://www.practiceportuguese.com/wp-content/uploads/2017/08/Household-Items.jpg"
    detection_reult = detect_product(IMAGE_URL)
    image = show_products(IMAGE_URL, detection_reult)
    image.show()
