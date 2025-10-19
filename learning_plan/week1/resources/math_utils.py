

import math
from re import S
from typing import Literal

def is_prime(n: int) -> Literal[False]:
    '''
    判断一个数是否为质数
    '''
    if n<2:
        return False
    elif n== 2:
        return True
    elif n>2 and n%2 == 0:
        #  判断是否为偶数
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True

def factorial(n: int) -> int:
    '''
    计算一个数的阶乘
    '''
    sum = 1
    for i in range(1,n+1):
        sum*=i
    return sum

def gcd(a: int, b: int) -> int:
    '''
    计算两个数的最大公约数
    '''
    return math.gcd(a, b)
    # while b != 0:
    #     a, b = b, a % b
    # return abs(a)  # 确保返回正数

if __name__ == "__main__":
    print(is_prime(11))
    print(factorial(5))
    print(gcd(10, 5))