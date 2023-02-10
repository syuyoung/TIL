import sys
input = sys.stdin.readline

li = []
for i in range(5):
    li.append(int(input()))
sort_li = sorted(li)
print(sum(sort_li)//5)
print(sort_li[2])