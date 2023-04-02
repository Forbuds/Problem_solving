import sys
input = sys.stdin.readline

n = int(input().strip())
w = list(map(int, input().strip().split()))
sum = 0
for i in range(n):
    # print(w.pop(w.index(min(w))))
    # print(('   ',n-1))
    sum+=(n-i)*w.pop(w.index(min(w)))
print(sum)