import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    # print(list(map(str,input().strip())))
    s = input().strip()
    # print(s)
    flag = True
    result = 0    #+1, -1
    tmp = s[0]
    for i in range(len(s)):
        # 첫 시작에 ) 이거 나오면 안됨  : r <0
        #
        # print(result)
        if s[i]==')':
            result -= 1

            if result < 0:
                # print('NO')
                break
                # print('나가')
        else:
            result += 1
    # print(result)
    if result >0 or result<0:  # 다 안
        print('NO')
    else:
        print('YES')




