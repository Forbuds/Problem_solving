# https://seongonion.tistory.com/98

import sys
input = sys.stdin.readline

n,s = map(int,input().strip().split())
g = list(map(int,input().strip().split()))

cnt = 0
def sub_sum(idx,s_s):
    global cnt
    if idx>=n:
        return
    s_s += g[idx]
    if s_s==s:
        cnt+=1

    sub_sum(idx + 1, s_s)

    sub_sum(idx+1,s_s-g[idx])

sub_sum(0,0)
print(cnt)