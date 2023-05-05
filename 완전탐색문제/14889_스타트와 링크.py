import sys
# input = sys.stdin.readline

n = int(sys.stdin.readline())
s = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# print(s)
result = sys.maxsize
## 최소값이니까 max값으로 시작한다.


# 생각의 흐름 : 경우의 수인가? 수가 작으니 완탐인 것 같다. 왜냐면 N이 20개밖에 없다.
# nC2/n정도인 것 같다.

# 와 근데 너무 많다. 그래서 방법을 찾아 보니 사람들이 backtracking으로 많이들 풀어 두었다.
# backtraking이란 ?
# 모든 경우의 수를 고려하면서, dfs, bfs
# 모든 경우의 수를 탐색하려면 일반적으로 dfs
# https://hgk5722.tistory.com/319


# 근데 백준 확인해 보니 combinations가 더 빠르게 풀 수 있는 방법이더라!

v = [False for _ in range(n)]

def bt(depth, idx):
    global result
    if depth == n//2:   #한 팀 완성 되었네
        r1, r2 = 0 , 0
        for i in range(n):
            for j in range(n):
                if v[i] and v[j]:   # 둘 다 1인 팀
                    r1+= s[i][j]
                elif not v[i] and not v[j]:  # 둘 다 0인 팀
                    r2+= s[i][j]
        result = min(result,abs(r1-r2))
        return

    for i in range(idx,n):
        if not v[i]:
            v[i]=True
            bt(depth+1, i+1)    # 이 부분 idx로 썼다가 틀림, 잘 볼 것
            v[i]=False
bt(0,0)
print(result)


