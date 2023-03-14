# tmp = list(map(int,input().strip()))
import sys
input = sys.stdin.readline

s = list(map(int,input().split()))
print(s)

#> 1234
# [1234]
#> 1 2 3 4
# [1, 2, 3, 4]

s = list(map(int,input()))
print(s)

# 1234
# '\n'

s = list(map(int,input().strip()))
print(s)
#> 1234
# [1, 2, 3, 4]
# >1 2 3 4
# ValueError: invalid literal for int() with base 10: ' '


s = list(map(int,input().strip().split()))
print(s)
# >1234
# [1234]
# >1 2 3 4
# [1, 2, 3, 4]