import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
g = []   # 단지를 나타낼 행렬

def print_g(g):
    for i in range(len(g)):
        print(g[i])

for _ in range(n):
    tmp = list(map(int,input().strip()))
    g.append(tmp)

# print_g(g)

v = [[0]*n for _ in range(n)]
from collections import deque
def bfs(x,y,building_group):
    c=1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque([(x,y)])
    v[x][y]=1
    while q:
        nx,ny = q.popleft()
        for i in range(4):
            cx,cy = nx+dx[i],ny+dy[i]
            if 0<=cx<n and 0<=cy<n:
                if v[cx][cy]==0 and g[cx][cy]==1:
                    v[cx][cy]=c
                    q.append((cx,cy))
                    c+=1
    building_group.append(c)   #bfs가 다끝나면 블럭 개수 업데이트


result = 0
building_group =[]
for x in range(n):
    for y in range(n):
        if g[x][y]==1 and v[x][y]==0:
            bfs(x,y,building_group)
            result+=1    # 단지 개수


# print_g(v)
print(result)
# print(building_group)
building_group.sort()
for i in range(len(building_group)):
    print(building_group[i])