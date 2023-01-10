# 1
T = int(input())

for t in range(1, T + 1):
    a, b = list(map(int,input().split()))
    x = a // b
    y = a % b
    print(f"#{t} {x} {y}")


# 2
T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int,input().split()))
    num = sum(numbers)
    print(f"#{t} {round(num / len(numbers))}")


# 3
import math

a, b = list(map(int,input().split()))
1 <= a
b <= 9
print(a+b)
print(a-b)
print(a*b)
print(math.floor(a//b))


# 4
number = int(input())
number <= 100000
for num in range(number):
    print('#', end='')


# 5
T = int(input())

for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    num = [x for x in numbers if 0 <= x <= 10000]
    a = max(num)
    
    print(f'#{t} {a}')