"""
    멀티 프로세스 풀 사용하기
"""
from multiprocessing import Pool


def squared(x: int) -> int:
    """ 제곱 하기 """
    return x * x


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(squared, [1, 2, 3]))