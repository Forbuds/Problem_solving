n,m,v_1 = map(int, input().split())
g = dict()
for i in range(m):
    a,b = map(int,input().split())
    g[a] = g.get(a,[])+[b]
    g[b] = g.get(b, []) + [a]
print(g)
print('dfs')

def dfs(g,v_1):
    v=[0]*(n+1)
    s = [v_1]
    v[v_1] = 1
    print(v_1,end=' ')
    while s:
        n_c = s.pop()
        if v[n_c]==0:
            v[n_c]=1
            print(n_c,end=' ')
        for n_a in sorted(g[n_c],reverse=True):
            if v[n_a]==0:
                s.append(n_a)
dfs(g,v_1)
print()
print('bfs')

def bfs(g,v_1):
    from collections import deque
    v = [0]*(n+1)
    v[v_1]=1
    s = deque([v_1])
    print(v_1)
    while s:
        n_c = s.popleft()
        for n_a in sorted(g[n_c]):
            if v[n_a]==0:
                v[n_a]=1
                s.append(n_a)
                print(n_a)
bfs(g,v_1)
'''
5 5 3
5 4
5 2
1 2
3 4
3 1
{5: [4, 2], 4: [5, 3], 2: [5, 1], 1: [2, 3], 3: [4, 1]}
dfs
3 1 2 5 4 
bfs
3 1 4 2 5 
'''

# https://velog.io/@dnflrhkddyd/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-BFS
# 다차원 배열에서 각 칸을 방문할 때 너비를 우선으로 방문하는 알고리즘
#  그러면 결국 우리는 다차원 배열에서 굳이 BFS 대신 DFS를 써야하는 일이 없다. Flood Fill은 BFS, DFS중에 어느 것을 써도 상관 없는데 거리측정은 BFS만 할 수 있으니 DFS를 쓸 일이 없다.
# 그래서 다차원배열에서 순회하는 문제를 풀때 BFS만 쓰면 된다.
# DFS는 나중에 그래프와 트리구조를 배울 때 필요하다.