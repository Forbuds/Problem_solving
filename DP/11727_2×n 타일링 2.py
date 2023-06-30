# n이 홀수면 무조건 앞에꺼 *1
# n이 짝수면 한 칸에 가능한 경우의 수 *2
import sys
input = sys.stdin.readline
n = int(input().strip())
l = [10007]*(1001)
l[1] = 1
l[2] = 3
for i in range(3,n+1):
    l[i] = l[i - 1] + l[i - 2] * 2
print(l[n]%10007)