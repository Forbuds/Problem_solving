
# https://velog.io/@kimdukbae/BOJ-10819-%EC%B0%A8%EC%9D%B4%EB%A5%BC-%EC%B5%9C%EB%8C%80%EB%A1%9C-Python
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().strip().split()))
result = 0
# print(a)
def sum_(a):
    global n
    s = 0
    for i in range(0,n-1):
        s += abs(a[i]-a[i+1])
    return s
# print(sum_(a))
v = [0 for _ in range(n)]
# print(v)
tmp = []
def max_diff(idx,arr):
    global result

    if idx >= n:
        # print(arr)
        # tmp.append(sum_(arr))
        result = max(result, sum_(arr))
        return

    for i in range(n):
        if v[i]==0:
            arr.append(a[i])
            v[i]=1
            max_diff(idx+1,arr)
            v[i]=0
            arr.pop()

max_diff(0,[])
print(result)
# print(tmp)