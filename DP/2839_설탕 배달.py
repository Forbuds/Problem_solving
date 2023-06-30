# # 일반 풀이
# import sys
# input = sys.stdin.readline
#
# sugar = int(input())
#
# result = 0
#
# while True:
#     if sugar >=0:
#         if sugar%5==0:
#             result += sugar//5
#             print(result)
#             break
#         sugar -=3
#         result +=1
#     else:
#         print(-1)
#         break

# DP
# [link](https://soopeach.tistory.com/47?category=997511)
import sys
input = sys.stdin.readline
n_list = [50000]*(5001)
n_list[3] = n_list[5] = 1
sugar = int(input().strip())
for i in range(6,sugar+1):
    n_list[i] = min(n_list[i-3],n_list[i-5]) + 1

if n_list[sugar]>=50000:
    print(-1)
else:
    print(n_list[sugar])