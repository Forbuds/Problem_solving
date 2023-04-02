import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())
# print(n,m)
c_list = list(map(int,input().strip().split()))
# print(c_list)

# for i in range(m):
#     tmp = [(c_list[i],i) for i in range(n)]
#     tmp.sort(reverse=True)
#     # print(tmp)
#     a,f_i = tmp.pop()
#     b,s_i = tmp.pop()
#     c_list[f_i] = a+b
#     c_list[s_i] = a + b
#     # print(c_list)
# print(sum(c_list))
for i in range(m):
    # print(c_list.index(min(c_list)))
    s = 0
    v = min(c_list)
    s+=c_list.pop(c_list.index(v))
    v = min(c_list)
    s+=c_list.pop(c_list.index(v))
    c_list.append(s)
    c_list.append(s)
# print(c_list)
print(sum(c_list))

# sorting과 pop의 시간 차이 알아두기