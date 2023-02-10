import sys

input = sys.stdin.readline
li = []
N = int(input())
for _ in range(N):
    li.append(int(input()))
s_li = sorted(li)

for i in s_li:
    print(i)