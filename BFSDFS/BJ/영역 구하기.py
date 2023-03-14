import sys
from collections import deque
input=sys.stdin.readline
def print_g(g):
    for i in range(len(g)):
        print(g[i])

m,n,k = map(int,input().strip().split())
# print(m,n,k)
g = [[0]*n for _ in range(m)]
for o in range(k):
    a,b,c,d = map(int,input().strip().split())
    a,b,c,d = m-b-1,a,m-d-1,c
    for i in range(b,d):
        for j in range(c+1,a+1):
            g[j][i]=o+1

# print_g(g)
answer = 0
v = [[0]*n for _ in range(m)]
block = []
def bfs(x,y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    c = 1
    q=deque([(x,y)])
    v[x][y]=1
    while q:
        nx,ny = q.popleft()
        for i in range(4):
            cx,cy = nx+dx[i],ny+dy[i]
            if 0<=cx<m and 0<=cy<n:
                if g[cx][cy]==0 and v[cx][cy]==0:
                    v[cx][cy]=1
                    c+=1
                    q.append((cx,cy))
    block.append(c)
for x in range(m):
    for y in range(n):
        if g[x][y]==0 and v[x][y]==0:
            bfs(x,y)
            answer +=1
print(answer)
for i in sorted(block):
    print(i,end=' ')

