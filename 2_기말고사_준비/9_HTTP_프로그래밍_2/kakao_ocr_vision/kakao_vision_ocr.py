"""
    카카오 API 사용하기: 비전 (OCR)
"""

import cv2
import requests

LIMIT_PX = 1024
LIMIT_BYTE = 1024 * 1024  # 1MB
LIMIT_BOX = 40


def kakao_ocr_resize(image_path: str) -> str or None:
    """ pixel 제약사항 체크 함수. 초과할 경우 resize 수행 """
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    if LIMIT_PX < height or LIMIT_PX < width:
        ratio = float(LIMIT_PX) / max(height, width)
        image = cv2.resize(image, None, fx=ratio, fy=ratio)
        cv2.imwrite(image_path, image)

        # api 사용전에 이미지가 resize된 경우, recognsize시 resize된 결과를 사용해야함.
        image_path = f"{image_path}_resized.jpg"

        return image_path
    return None


def kakao_ocr(image_path: str, rest_api_key: str) -> requests.models.Response:
    """ ocr API 호출 """
    API_URL = "https://dapi.kakao.com/v2/vision/text/ocr"

    headers = {"Authorization": f"KakaoAK {rest_api_key}"}

    return requests.post(API_URL,
                         headers=headers,
                         files={"image": open(image_path, "rb")})


def main() -> None:
    """ 메인 함수 """
    image_path = "kakao_text.jpg"
    REST_API_KEY = '447145f6d9f94e5468fc93b5eaba9be6'

    resize_impath = kakao_ocr_resize(image_path)
    if resize_impath is not None:
        image_path = resize_impath
        print("원본 대신 리사이즈된 이미지를 사용합니다.")

    output = kakao_ocr(image_path, REST_API_KEY).json()
    print(f"[OCR] output: \n{output}\n")


if __name__ == '__main__':
    main()