
# 이렇게 해서 예제 1 5, 예제 2 6으로 맞았지만 제출하면 틀렸다. 마지막 아무 지역도 물에 잠기지 않을 수도 있다. 를 고려하지 않아서 일수도?
# 일단 나랑 비슷하게 푼 링크 : https://lakelouise.tistory.com/78
# https://hidemasa.tistory.com/143
import sys
from collections import deque
import copy
input = sys.stdin.readline

n = int(input())
g = []


def print_g(g):
    for i in range(len(g)):
        print(g[i])
lim=0
k=0
g_=[]
for _ in range(n):
    # print(list(map(int, input().strip().split())))
    tmp = list(map(int, input().strip().split()))

    # for j in range(n):
    #     if tmp[j]<=k+1:
    #         tmp[j]=0
    #     else:
    #         tmp[j]=1

    g_.append(tmp)
while(1):

    # print(k)


    def bfs(x,y):
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        q = deque([(x,y)])
        v[x][y]=1
        while q:
            (nx,ny) = q.popleft()
            for i in range(4):
                cx,cy = nx+dx[i],ny+dy[i]
                if 0<=cx<n and 0<=cy<n:
                    if v[cx][cy]==0 and g[cx][cy]==1:
                        v[cx][cy] = 1
                        q.append((cx,cy))


    g = copy.deepcopy(g_)#[g_[i] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if g[i][j]<=k+1:
                g[i][j]=0
            else:
                g[i][j]=1
    # print_g(g)
    # s = 0
    # for i in range(len(g)):
    #     s += sum(g[i])
    # if s

    v = [[0]*n for _ in range(n)]
    a = 0
    for x in range(n):
        for y in range(n):
            if v[x][y]==0 and g[x][y]==1:
                bfs(x,y)
                a+=1
    # print(a)
    if a<lim:
        break
    else:
        lim=a
    k+=1

'''
import sys
from collections import deque
import copy
input = sys.stdin.readline

n = int(input())
g = []

for _ in range(n):
    tmp = list(map(int, input().strip().split()))
    g.append(tmp)

mv = 0
for i in range(n):
    mv =max(max(g[i]),mv)
# print(mv)

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(x,y):
    q = deque([(x,y)])
    v[x][y]=1
    while q:
        (nx,ny) = q.popleft()
        for i in range(4):
            cx,cy = nx+dx[i],ny+dy[i]
            if 0<=cx<n and 0<=cy<n:
                if v[cx][cy]==0 and g[cx][cy]>k:
                    v[cx][cy] = 1
                    q.append((cx,cy))
b_arr = []
for k in range(0,mv+1):
    v = [[0]*n for _ in range(n)]
    a = 0
    for x in range(n):
        for y in range(n):
            if v[x][y]==0 and g[x][y]>k:
                bfs(x,y)
                a+=1
    b_arr.append(a)
    # print(a)

print(max(b_arr))

# 추가예제
# 5
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
#
# 1
#
# 2
# 1 1
# 1 1
#
# 1


'''