# https://velog.io/@grace0st/%EA%B3%B1%EC%85%88-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC


import sys
input = sys.stdin.readline
a,b,c = map(int, input().strip().split())
print(a,b,c)


def multi(a, n):
    if n == 1:
        return a % c
    else:
        tmp = multi(a, n // 2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c


print(multi(a, b))