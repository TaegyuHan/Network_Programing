"""
   카카오 API 사용하기: 비전 (얼굴 검출)
"""
import PIL.JpegImagePlugin
import requests
from PIL import Image, ImageFilter

API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
REST_API_KEY = '토큰'


def detect_face(filename: str) -> dict:
    """ 얼굴 인식 """
    # app_key와 이미지 파일을 POST로 전송하여 얼굴 검출을 수정
    headers = {"Authorization": f"KakaoAK {REST_API_KEY}"}
    files = {"image": open(filename, "rb")}
    rsp = requests.post(API_URL, headers=headers, files=files)
    return rsp.json()  # 검출 결과 Json

def mosaic(filename: str, detection_reult: dict) -> PIL.JpegImagePlugin.JpegImageFile:
    """ 모자이크 처리 """
    image = Image.open(filename)

    for face in detection_reult["result"]["faces"]:
        x = int(face["x"] * image.width)   # 반환되는 x, y, w, h 값은
        y = int(face["y"] * image.height)  # 0 ~ 1.0 사이의 비율이 므로
        w = int(face["w"] * image.width)   # 실제 크기를 곱해야
        h = int(face["h"] * image.height)  # 좌표값을 얻을 수 있음
        box = image.crop((x, y, x + w, y + h)) # 얼굴 부분 잘라내기

        # 모자이크 처리
        box = box.resize((20, 20), Image.Resampling.NEAREST).resize((w, h), Image.Resampling.NEAREST)
        image.paste(box, (x, y, x + w, y + h)) # 모자이크 부분 다시 붙이기

    print(type(image))
    return image


if __name__ == '__main__':
    IMAGE = "test_image.jpg"
    detection_result = detect_face(IMAGE)
    image = mosaic(IMAGE, detection_result)
    image.show()