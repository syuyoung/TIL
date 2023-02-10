import sys
input = sys.stdin.readline

li = []
N = int(input())
for i in range(N):
    li.append(int(input()))
sort_li = sorted(li)
print(round(sum(sort_li)/N))
print(sort_li[N//2])
from collections import Counter
cnt = Counter(sort_li)
result = cnt.most_common()
if len(result) > 1:
    if result[0][1] == result[1][1]:
        print(result[1][0])
    else:
        print(result[0][0])
else:
    print(result[0][0])

print(max(sort_li)-min(sort_li))