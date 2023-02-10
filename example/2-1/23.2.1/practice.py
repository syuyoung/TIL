# 2525

import sys

input = sys.stdin.readline

a,b = map(int,input().split())
c = int(input())

hours = int((a*60+b+c)/60)
minutes = int((a*60+b+c)%60)
if(hours>23):
    hours = hours-24
print(hours, minutes)

2798

import sys

input = sys.stdin.readline

n, m = map(int,input().split())
card = list(map(int,input().split()))

result = 0
for i in range(n-2):
    for j in range(i + 1, n-1):
        for k in range(j + 1, n):
            sum = card[i] + card[j] + card[k]

            if sum <= m:
                result = max(result, sum)
print(result)


# 9076
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(1, T+1):
        score = list(map(int, input().split()))
        score = sorted(score)
        if score[-2]-score[1] >= 4:
            print('KIN')
        else:
            print(sum(score[1:4]))
sys.stdin = open("input.txt", "r")

#
import sys

input = sys.stdin.readline
n = int(input())

for i in range(n, n+1):
    if i%4