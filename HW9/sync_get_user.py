import time

def get_user(name):
    print(f"사용자 {name} 정보 조회중...")
    time.sleep(1)
    print(f"사용자 {name} 정보 조회 완료!")

def main():
    start = time.time()
    get_user("Jeon")
    get_user("Yun")
    get_user("Kim")
    get_user("Song")
    end = time.time()
    print(f"총 소요시간: {end - start}")

main()