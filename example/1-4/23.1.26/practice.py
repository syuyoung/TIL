# 10101
a = int(input())
b = int(input())
c = int(input())
if a == b == c == 60:
    print('Equilateral')
elif a+b+c == 180:
    if a == b or b == c or a == c:
        print('Isosceles')
    else:
        print('Scalene')
elif a+b+c != 180:
    print('Error')

# 2720

T = int(input())

for i in range(1, T+1):
    N = int(input())
    coin = [25, 10, 5, 1]
    result = []
    for i in coin:
        result.append(N//i)
        N %= i
    print(*result)


# 1453

N = int(input())
numbers = map(int, input().split())
list = []
cnt = 0
for i in numbers:
    if i not in list:
        list.append(i)
    elif i in list:
        cnt += 1
print(cnt)

# 10773

N = int(input())
stack = []
for i in range(N):
    number = int(input())

    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))

# 2161

from collections import deque

n = int(input())
queue = deque(range(1, n+1))

while len(queue) > 1:
    print(queue.popleft(), end=' ')
    queue.append(queue.popleft())

print(queue[0])

# 9012

T = int(input())
for i in range(1, T+1):
    word = list(input())
    cnt = 0
    for i in word:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
    if cnt == 0:
        print('YES')
    elif cnt >0:
        print('NO')