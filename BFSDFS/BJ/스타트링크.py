# https://door-of-tabris.tistory.com/entry/%EB%B0%B1%EC%A4%80-5014%EB%B2%88-%EC%8A%A4%ED%83%80%ED%8A%B8%EB%A7%81%ED%81%AC%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://velog.io/@ms269/%EB%B0%B1%EC%A4%80-5014-%EC%8A%A4%ED%83%80%ED%8A%B8%EB%A7%81%ED%81%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
# 바로 위에 코드가 진짜
from collections import deque
import sys
input = sys.stdin.readline

f,s,g,u,d = map(int,input().rstrip().split())
# print(f,s,g,u,d)
dn = [u,-d]
def bfs(s):
    q = deque([s])
    v[s]=0
    while q:
        nc = q.popleft()
        if nc==g:
            return v[nc]
        for i in range(len(dn)):
            cn = nc+dn[i]
            if 0<cn<=f and v[cn]==-1:
                v[cn]=v[nc]+1
                q.append(cn)
    return "use the stairs"




v = [-1 for i in range(f+1)]
print(bfs(s))
