# n = int(input())
# card = list(range(1,n+1))
# while len(card) > 1:
#     print(card.pop(0), end=' ')
#     card.append(card.pop(0))
# print(card[0])

import sys
input = sys.stdin.readline()

K = int(input)
stack = []

for i in range(K):
    num = int(input)
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))