# # 2441

# N = int(input())
# for i in range(1, N+1):
#     print(' '*(i-1)+'*'*(N-i+1))

# 2592


# import sys

# N_list = [int(sys.stdin.readline()) for _ in range(10)]

# print(sum(N_list)//10)
# print(max(N_list, key = N_list.count))

#10798
import sys
sys.stdin = open("input.txt", "r")

matrix = [input() for _ in range(5)]
for i in range(15):
    for j in range(5):
        if i < len(matrix[j]):
            print(matrix[j][i], end='')