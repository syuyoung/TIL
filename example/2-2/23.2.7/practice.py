#17608

import sys
input = sys.stdin.readline

N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))

r_li = reversed(li)

cnt = 0
max = 0

for i in r_li:
    if max < i:
        max = i
        cnt += 1
print(cnt)
# #7568

import sys
input = sys.stdin.readline

N = int(input())
li = []
for _ in range(N):
    number = list(map(int,input().split()))
    li.append(number)

for i in range(N):
    result = 1
    for j in range(N):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            result +=1
    print(result, end=' ')

