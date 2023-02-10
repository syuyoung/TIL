import sys
input = sys.stdin.readline
li = []
N = input()
for i in N:
    li.append(i)
li.pop()
s_li = sorted(li,reverse=True)
for i in s_li:
    print(i, end='')