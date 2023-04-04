import sys
input = sys.stdin.readline

arr = input().strip().split('-')
# print(arr)
# 값을 최소로?
# 최대한 큰걸 빼야 한다.
s = 0
for i,arr_tmp in enumerate(arr):
    # print(arr_tmp)
    tmp = 0
    for n in arr_tmp.split('+'):
        tmp+=int(n)
    if i==0:
        s+=tmp
    else:
        s-=tmp
    # print(tmp)
    # print('s', s)

print(s)

# 혼자 풀어볼 것, 아래는 참고했던 블로그
# https://sungmin-joo.tistory.com/67
# https://sodehdt-ldkt.tistory.com/49