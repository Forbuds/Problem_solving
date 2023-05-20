l = []
for _ in range(7):
    n = int(input())
    if n%2==1:
        l.append(n)
if len(l)==0:
    print(-1)
else:
    print(sum(l))
    print(min(l))