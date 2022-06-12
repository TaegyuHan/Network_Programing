"""
    해시 함수

    SHA : Secure Hash Algorithm 알고리즘이 가장 많이 사용됨

    생성되는 해시 값의 크기에 따라 SHA-1(160비트), SHA-256(256비트) 등이 있음
"""

from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256())
digest.update(b"abc")
digest.update(b"123")
hash = digest.finalize()
print(hash)
# b'l\xa1=R\xcap\xc8\x83\xe0\xf0\xbb\x10\x1eBZ\x89\xe8bM\xe5\x1d\xb2\xd29%\x93\xafj\x84\x11\x80\x90'

digest = hashes.Hash(hashes.SHA256())
digest.update(b"abc123")
hash = digest.finalize()
print(hash)
# b'l\xa1=R\xcap\xc8\x83\xe0\xf0\xbb\x10\x1eBZ\x89\xe8bM\xe5\x1d\xb2\xd29%\x93\xafj\x84\x11\x80\x90'

digest = hashes.Hash(hashes.SHA256())
digest.update(b"abc124")
hash = digest.finalize()
print(hash)
# b'\xcdp\x11\xe7\xa6\xb2}D\xce"\xa7\x1aL\xdf\xc2\xc4}\\g\xe351\x9e\xd7\xf6\xaer\xcc\x03\xd7\xd6?'