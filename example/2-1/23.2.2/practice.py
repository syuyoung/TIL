# 1547

import sys
input = sys.stdin.readline

ball = 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == ball:
        ball = b
    elif b == ball:
        ball = a
print(ball)

# 5576

import sys

input = sys.stdin.readline

w = [int(input()) for _ in range(10)]
w = sorted(w)
k = [int(input()) for _ in range(10)]
k = sorted(k)
print(sum(w[-3:]), sum(k[-3:]))

# 2846

import sys
input = sys.stdin.readline

n = int(input())
way = list(map(int, input().split()))
num = 0
result = []

for i in range(n-1):
    if way[i] < way[i+1]:
        num += way[i+1] - way[i]

    elif way[i] >= way[i+1]:
        result.append(num)
        num = 0
    
result.append(num)
print(max(result))

# 1251

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
