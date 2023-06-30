import sys
input  = sys.stdin.readline

n = int(input().strip())

s=[]
for _ in range(n):
    s.append(input().strip())
s = list(set(s))
s  = sorted(s,key=lambda x: [len(x),x])
for i in range(len(s)):
    print(s[i])