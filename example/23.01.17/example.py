# 10818

N = input()
numbers = list(map(int,input().split()))
print(min(numbers), max(numbers))

# 11720

N = input()
print(sum(map(int,input())))

# 2750
N = int(input())
result = []
for i in range(N):
    result.append(int(input()))
result.sort()

for num in result:
    print(num)

# 2562

result = []
for i in range(9):
    result.append(int(input()))

m = max(result)
n = result.index(max(result))
print(m)
print(n+1)