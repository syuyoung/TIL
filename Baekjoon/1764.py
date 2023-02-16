import sys

n, m = map(int,input().split())
nlist = set()
mlist = set()
for _ in range(n):
    nlist.add(input())
for _ in range(m):
    mlist.add(input())

result = sorted(list(nlist & mlist))

print(len(result))

for i in result:
    print(i)