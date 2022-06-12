"""
    대칭키 암호

    AES : Advanced Encryption Standard

        - 미국 표준 기술 연구소NIST는 2001년 11월 26일 AES를 FIPS-197으로 공포

        - 사용되는 키의 크기에 따라 AES-128, AES-192, AES-256 등이 있음

        특징
        - 암호화와 복호화 속도가 비대칭 키 암호에 비해서 빨라서 WiFi, LTE/5G 등에서 널리
            사용됨

        - 서로 동일한 키를 미리 안전하게 공유하여야 함. 온라인 환경에서는 쉽지 않음
"""

from cryptography.fernet import Fernet

key = Fernet.generate_key()  # 128bit 생성
# b'P2W8zY1NAUWPPbeFyUHeTTJZm0AU66UTDfjKwylJpwI='
print(key)

cipher_suite = Fernet(key)

cipher_text = cipher_suite.encrypt(b"Internet of Things")
plain_text = cipher_suite.decrypt(cipher_text)

print("Encrypted Text: ", cipher_text)
print("Decrypted Text: ", plain_text)