import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def print_g(g):
    for i in range(len(g)):
        print(g[i],'_ok')

n = int(input().strip())
g = []
print()
for i in range(n):
    # print(list(map(int,input().strip().split(' '))))
    g.append(list(map(int,input().strip().split())))

print(n)
print_g(g)
# g = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
# ch = g[0][0]
result=[]
def make_p(x,y,N):
    ch = g[x][y]

    for i in range(x,x+N):
        for j in range(y,y+N):
            if ch!=g[i][j]:
                make_p(x,y,N//2)
                make_p(x+N//2, y, N // 2)
                make_p(x, y+N//2, N // 2)
                make_p(x+N//2, y+N//2, N // 2)
                return
    if ch==0:
        result.append(0)
    else:
        result.append(1)

make_p(0,0,n)

print(result.count(0))

print(result.count(1))
# pass
#             else:
#                 for ik in range(2):
#                     for jk in range(2):
#                         g_ = g[ik*len_g:(ik+1)*len_g][jk*len_g:(jk+1)*len_g]
#                         print(ik*len_g,(ik+1)*len_g,jk*len_g,(jk+1)*len_g,g_)
#                         make_p(g_)
#     print('same, ', g)
#     return
