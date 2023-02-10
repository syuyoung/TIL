import sys
input = sys.stdin.readline
result = []
numbers = list(map(int,input().split()))
for i in numbers:
    num = i**2
    result.append(num)
print(sum(result)%10)