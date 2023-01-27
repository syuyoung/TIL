10817

import sys

input = sys.stdin.readline

numbers = list(map(int,input().split()))
numbers = sorted(numbers)
print(numbers[1])

# 20001

start = input()
cnt = 0
while True:
    word = input()
    if word == '문제':
        cnt +=1
    elif word == '고무오리':
        if cnt == 0:
            cnt += 2
        else:
            cnt -= 1
    elif word == '고무오리 디버깅 끝':
        break

if cnt == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')

# 1269
import sys

input = sys.stdin.readline

A,B = map(int,input().split())
set_A = set(map(int,input().split()))
set_B = set(map(int,input().split()))

print(len(set_A-set_B)+len(set_B-set_A))

# 1181

import sys

input = sys.stdin.readline

N = int(input())
word = []
for _ in range(N):
    word.append(input().strip())

word= list(set(word)) 
word.sort()
word.sort(key=len)

for i in range(len(word)):
    print(word[i])

# 11286

import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):