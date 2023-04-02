import sys
input = sys.stdin.readline
n = int(input())
g = []
# print(n)
for i in range(n):
    g.append(list(map(int,input().strip().split())))

result = []
def paper(x,y,N):
    ch = g[x][y]
    k = N//3
    for i in range(x,x+N):
        for j in range(y,y+N):
            if ch!=g[i][j]:
                for a in range(3):
                    for b in range(3):
                        paper(x+a*k,y+b*k,k)
                return
    result.append(ch)
paper(0,0,len(g))
# print(result)
print(result.count(-1))
print(result.count(0))
print(result.count(1))
'''
x,y = 0,0
k=3//3
for a in range(3):
    for b in range(3):
        print(x+a*k,x+(a+1)*k,y+b*k,y+(b+1)*k)

        '''

# https://zidarn87.tistory.com/385