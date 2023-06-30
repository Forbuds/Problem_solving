# 홀수일 때 1
# 짝수일 때 2

import sys
input = sys.stdin.readline

n = int(input().strip())
dp = [0]*1001
dp[1]=1
dp[2] = 2
# dp[3] = dp[2]
# dp[4] = dp[3]+dp[2]
for i in range(3,n+1):
    dp[i] = dp[i - 1] + dp[i - 2]
    # if i%2==0:
    #     dp[i] = dp[i-1]+dp[i-2]
    # else:
    #     dp[i] = dp[i-1]
print(dp[:n])
print(dp[n]%10007)