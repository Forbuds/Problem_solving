import sys

input = sys.stdin.readline
g =[]
n = int(input().strip())
for _ in range(n):
    g.append(list(map(int,input().strip().split())))

# v =[ [0]*(n) for _ in range(n)]
s =[]
v = [0]*(n)
idx = []
result = 1000000*5
def dfs(k):
    global result
    if len(s)==n-1:
        # print(sum(s))
        if g[idx[-1][1]][idx[0]]!=0:
            result = min(result,sum(s)+g[idx[-1][1]][idx[0]])
            # print(s, idx[-1][1],idx[0])
            # print(s,sum(s)+g[idx[-1][1]][idx[0]])
            # print(idx,idx[-1][1],idx[0])
            return
        else:
            # result = result
            return
    else:
        for i in range(n):
            if v[i]==0 and g[k][i]!=0:
                v[i]=1
                s.append(g[k][i])
                idx.append((k,i))
                dfs(i)
                v[i]=0
                s.pop()
                idx.pop()
for i in range(n):
    v[i]=1
    idx.append(i)
    dfs(i)
    v[i]=0
    idx.pop()
print(result)