import sys
input = sys.stdin.readline

li = []
for _ in range(3):
    N = int(input())
    li.append(N)
s_li = sorted(li)
print(s_li[1])