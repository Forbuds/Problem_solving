# <https://fre2-dom.tistory.com/491>
# <https://chldkato.tistory.com/41>


import sys
input = sys.stdin.readline
from collections import deque

def print_g(g):
    for i in range(len(g)):
        print_k(g[i])
def print_k(g):
    for i in range(len(g)):
        print(g[i])


dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
def bfs(i,j,k):
    q = deque([(i,j,k)])
    v[i][j][k] = 1
    while q:
        z,x,y = q.popleft()
        for ii in range(6):
            nx = x+dx[ii]
            ny = y+dy[ii]
            nz = z+dz[ii]

            if 0<=nz<l and 0<=nx<r and 0<=ny<c:
                if g[nz][nx][ny]=='E':
                    # print('done : ',v[z][x][y])
                    print('Escaped in '+str(v[z][x][y])+' minute(s).')
                    return
                if g[nz][nx][ny]=='.' and v[nz][nx][ny]==0:
                    v[nz][nx][ny]=v[z][x][y]+1   # 덧셈으로 진행
                    q.append((nz,nx,ny))
    print('Trapped!')   #모든 q를 돌아도 나올 수 없을 때

while True:
    l,r,c = map(int,input().strip().split())
    # print(l,r,c)
    if l==0 and r==0 and c==0:
        break
    g =[[] for _ in range(l)]

    for i in range(l):
        for _ in range(r):
            g[i].append(list(map(str,input().strip())))
        sys.stdin.readline()

    v = [[ [0]*(c) for _ in range(r)] for _ in range(l)]

    # print_g(g)
    # print_g(v)
    # print(g)
    # print(v)

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if g[i][j][k]=='S':
                    bfs(i,j,k)



