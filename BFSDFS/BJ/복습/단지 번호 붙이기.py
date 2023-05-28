import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g = []
for _ in range(n):
    # print(list(map(int, input().strip())))
    g.append(list(map(int, input().strip())))
v = [[0]*n for _ in range(n)]
# print(v)

g_list = []
def bfs(i,j):
    c = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    s = deque([])
    s.append((i,j))
    v[i][j] = 1
    while s:
        i_c,j_c = s.popleft()
        for k in range(4):
            i_n,j_n = i_c+dx[k], j_c + dy[k]
            if 0<=i_n<n and 0<=j_n<n:
                if v[i_n][j_n]==0 and g[i_n][j_n] ==1:
                    v[i_n][j_n]=c
                    s.append((i_n,j_n))
                    c+=1
    g_list.append(c)
result = 0
for i in range(n):
    for j in range(n):
        if v[i][j] == 0 and g[i][j]==1:
            bfs(i,j)
            result +=1
print(result)
for i in sorted(g_list):
    print(i)