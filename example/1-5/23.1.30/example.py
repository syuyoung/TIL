# # 1225

# import sys

# a,b = sys.stdin.readline().split()

# a = list(map(int,a))
# b = list(map(int,b))
# print(sum(a)*sum(b))

# # 2438

# [print('*' * i) for i in range(1, int(input())+1)]


# # 2739

# n = int(input())
# for i in range(1, 10):
#     print(f'{n} * {i} = {n*i}')


# 2953

import sys
input = sys.stdin.readline
result = 0
num = 0
for i in range(5):
    N = sum(map(int,input().split()))
    if N > result:
        result = N
        num = i+1
print(num,result)