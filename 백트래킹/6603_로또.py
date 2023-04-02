import sys
input = sys.stdin.readline
def dfs(c):
    if len(w)==6:
        print(' '.join(map(str, w)))
    else:
        for i in range(c,k):
            if v[i]==0:
                w.append(s[i])
                v[i]=1
                dfs(i)
                w.pop()
                v[i]=0

# 중복허용 놉,

while True:
    w = []
    k = list(map(int, input().strip().split()))
    if k[0]==0:
        break
    elif k[0]<=6:
        break
    else:
        s = sorted(k[1:])
        k = k[0]
        v = [0]*k
        dfs(0)
    print()
