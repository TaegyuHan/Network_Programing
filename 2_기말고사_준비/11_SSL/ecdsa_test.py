"""
    디지털 서명 알고리즘

    DSA : Digital Signature Algorithm 또는
    ECD : SAElliptic Curve Digital Signature Algorithm가 널리 사용됨
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature


# 비밀키
private_key = ec.generate_private_key(
    ec.SECP384R1()
)

# 데이터
data = b"this is some data I'd like to sign"
signature = private_key.sign(
    data,
    ec.ECDSA(hashes.SHA256())
)
print(signature)

try:
    public_key = private_key.public_key()  # 공유 키
    public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))  # 데이터 변형 확인
except InvalidSignature:
    print("Invalid signature !!!!")

signature = signature + b"a" # 데이터 변경
print(signature)
try:
    public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
except:
    print("Invalid signature !!!!")