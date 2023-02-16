import sys

li = []
result = {}
N = int(input())
for _ in range(N):
    word = input()
    s_word = word.split('.')
    li.append(s_word[-1])

s_li = sorted(li)
for i in s_li:
    if i in result.keys():
        result[i] += 1
    else:
        result[i] = 1
for key, value in result.items():
    print(key, value)