import sys
input = sys.stdin.readline

n = int(input())
result = 0

for i in range(n):
    s = input().strip()
    if (len(s))<=1:
        result+=1
    else:
        tmp = set()
        tmp.add(s[0])
        key = True
        for j in range(1,len(s)):
            if s[j] in tmp and s[j-1]!=s[j]:
                key = False
            tmp.add(s[j])

        if key:
            result+=1

print(result)