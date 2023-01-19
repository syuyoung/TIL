# A = int(input())
# print(A-543)

# set = list(map(int,input().split()))
# chess = [1, 1, 2, 2, 2, 8]
# for i in range(len(set)):
#     set[i]=chess[i]-set[i]
# print(*set)

N, X = list(map(int,input().split()))
numbers = list(map(int,input().split()))
for i in numbers:
    if i < X:
        print(i)