"""
    카카오 API 사용하기: 비전 (멀티태그 생성)
"""

import argparse
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

API_URL = "https://dapi.kakao.com/v2/vision/multitag/generate"
REST_API_KEY = '토큰'


def generate_tag(image_url: str) -> None:
    """ 태그 반환 """
    headers = {"Authorization": f"KakaoAK {REST_API_KEY}"}

    data = {"image_url": image_url}
    resp = requests.post(API_URL, headers=headers, data=data)
    result = resp.json()["result"]

    if len(result["label_kr"]) > 0:
        print(f"이미지를 대표하는 태그는 \"{', '.join(result['label_kr'])}\"")
    else:
        print("이미지로부터 태그를 생성하지 못했습니다.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Classify Tags")
    parser.add_argument("image_url",
                        type=str,
                        nargs="?",
                        default="https://w7.pngwing.com/pngs/632/327/png-transparent-man-wearing-white-t-shirt-riding-bicycle-bicycle-pedal-architecture-manhattan-brooklyn-cycling-texture-bicycle-frame-bicycle.png",
                        help="image url to classify")

    args = parser.parse_args()

    generate_tag(args.image_url)

