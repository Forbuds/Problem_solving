# 1,2,3,4,5,6,7
# 0,1,2,3,4,5,6
# 0 + 2
# 3
#
#
# 1,2,4,5,6,7
# 0,1,2,3,4,5
# 2+2
# 6
#
# 1,2,4,5,7
# 0,1,2,3,4
# 4+2  (-5)  = 1
# 2
#
# 1,4,5,7
# 0,1,2,3
# 1+2 = 3
# 7
#
# 1,4,5
# 0,1,2
# 3+2-3 = 2
# 5

import sys
input = sys.stdin.readline

n,k = map(int, input().strip().split())
k-=1
s_i = 0
l = [i+1 for i in range(n)]
result = []

def ch_i(i,l):
    # print('input',i,len(l),l)
    if i>=len(l):
        return ch_i(i-len(l),l)
    else:
        return i

while True:
    if len(l)==0:
        break
    else:
        s_i = ch_i(s_i+k,l)
        result.append(str(l.pop(s_i)))
print('<'+', '.join(result)+'>')