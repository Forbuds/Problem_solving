import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
b = [e for e in enumerate(b)]
b.sort(key= lambda x:(-x[1]))
print(n,a,b)

# def mul_(x,y):
#     result = 0
#     for i in range(len(x)):
#         result += x[i]*y[i]
#     return result
#
# if __name__ == "__main__":

# v = [0 for _ in range(n)]
# result = []
#
# b =