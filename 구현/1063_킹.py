import sys

input = sys.stdin.readline
# print(map(str,input().strip().split()))
p_k, p_s, n = map(str,input().strip().split())
x = ['A','B','C','D','E','F','G','H']
y = [1,2,3,4,5,6,7,8]    # 행렬이랑 상관 없이 만들어 둔다.
kx = x.index(p_k[0])
ky = y.index(int(p_k[1]))
# print(kx,ky)

sx = x.index(p_s[0])
sy = y.index(int(p_s[1]))

# print(x.index(p_k[0]))
# print(y.index(int(p_k[1])))
# print([p_k, p_s, n])
# n이 50보다 자거나 가은 자연수라고 한다.
m = ['R','L','B','T','RT','LT','RB','LB']
n = int(n)
dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,1,-1,-1]

# 첫 번째 제출
tsx,tsy=sx,sy
for _ in range(n):
    p = str(input().strip())
    i = m.index(p)
    tx = kx+dx[i]
    ty = ky+dy[i]
    if tx==sx and ty==sy:
        tsx = sx+dx[i]
        tsy = sy+dy[i]
    else:
        tsx, tsy = sx, sy
    if 0<=tx<8 and 0<=ty<8 and 0<=tsx<8 and 0<=tsy<8:
        kx, ky = tx, ty
        sy, sx = tsy, tsx
    # print('s')
    # print(x[kx], str(y[ky]), x[sx], y[sy])
    # print(x[tx],str(y[ty]),x[tsx],y[tsy])



# A2 A1 2
# B
# T
# 반례입니다. 힌트 드리자면 돌 위치의 temp 저장을 다시 확인해보셔요!