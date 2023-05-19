import sys
input = sys.stdin.readline

t = int(input())
# print(t)
def change_i(k):
    if k<0:
        return 6+k
    elif k>5:
        return k-6
    else:
        return k
    # -5 -4 -3(3) -2(4) -1(5)< 0 1 2 3 4 5 < 6(0) 7(1) 8(2) 9 10
for _ in range(t):
    n = int(input())
    l = list(map(int, input().strip().split()))
    # print(n,l)
    d = 1
    while True:
        if sum(l)<=n:
            # print('ok')
            l_next = [l[change_i(i)] + l[change_i(i + 1)] + l[change_i(i - 1)] + l[change_i(i + 3)] for i in
                      range(len(l))]
            l = l_next
            d+=1
        else:
            # print('no')
            print(d)
            break
