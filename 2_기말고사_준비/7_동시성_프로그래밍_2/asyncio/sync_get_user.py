"""
    코루틴 예제: 사용자 정보 조회 프로그램
     - 동기
"""

import time


def get_user(name: str) -> None:
    """ 유저 정보 출력 """
    print(f"사용자 '{name}' 정보 조회중...")
    time.sleep(1)
    print(f"사용자 '{name}' 정보 조회 완료!")


def main() -> None:
    """ 메인 함수 """
    start = time.time()
    get_user("Jeon")
    get_user("Yun")
    get_user("Kim")
    get_user("Song")
    end = time.time()
    print(f"총 소요시간: {end - start}")


if __name__ == '__main__':
    main()