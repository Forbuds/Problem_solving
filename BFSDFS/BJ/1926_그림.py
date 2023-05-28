import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().strip().split())
g = []
v = [[0]*m for _ in range(n)]
for _ in range(n):
    g.append(list(map(int,input().strip().split())))
def bfs(x,y,max_p):
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    c = 1
    q = deque([(x,y)])
    v[x][y] = 1
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx,ny = cx+dx[k], cy+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if g[nx][ny]==1 and v[nx][ny]==0:
                    v[nx][ny]=c
                    q.append((nx,ny))
                    c+=1
    max_p = max(c,max_p)
    return max_p



result = 0
max_p = -1
if all(1 not in a for a in g):
    print(0)
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if g[i][j]==1 and v[i][j]==0:
                max_p = bfs(i,j,max_p)
                result+=1
    print(result)
    print(max_p)