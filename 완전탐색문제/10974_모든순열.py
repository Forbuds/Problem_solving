import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

def dfs(s):
    if s==n:
        print(*list(q))
        return
    else:
        for i in range(1,n+1):
            if v[i]==0:
                q.append(i)
                v[i]=1
                dfs(s+1)
                q.pop()
                v[i]=0

v=[0]*(n+1)
q = deque([])
dfs(0)




# import sys
# input = sys.stdin.readline
#
# n = int(input().strip())
# v = [0]*(n+1)
# s = []
#
# def dfs():
#     if len(s)==n:
#         print(*s)
#         return
#     else:
#         for i in range(1,n+1):
#             if v[i]==0:
#                 s.append(i)
#                 v[i]=1
#                 dfs()
#                 s.pop()
#                 v[i]=0
# dfs()