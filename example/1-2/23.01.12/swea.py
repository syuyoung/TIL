# 1
T = int(input())

for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    result = []
    for i in numbers:
        if i % 2 == 1:
            result.append(i)
    print(f'#{t} {sum(result)}')

# 2

T = int(input())

for t in range(1, T+1):
    num = input()
    month = int(num[4:6])
    day = int(num[6:8])
    if month in (1,3,5,7,8,10,12):
        if day <= 31:
            print(f'#{t} {num[0:4]}/{num[4:6]}/{num[6:8]}')
        else:
            print(f'#{t} -1')
    elif month in (4,6,9,11):
        if day <= 30:
            print(f'#{t} {num[0:4]}/{num[4:6]}/{num[6:8]}')
        else:
            print(f'#{t} -1')
    elif month == 2:
        if day <= 28:
            print(f'#{t} {num[0:4]}/{num[4:6]}/{num[6:8]}')
        else:
            print(f'#{t} -1')
    else:
        print(f'#{t} -1')
        


# 3

a, b = list(map(int,input().split()))

result = a-b+1
print(result)


# 4

num = int(input())
result = []
for i in range(1, num+1):
    if num%i == 0:
        result.append(i)

print(*result)


# 5

T = int(input())

for x in range(1, T+1):
    num = int(input())
    count = 0
    result = []
    for i in range(num):
        result= i*count+1
    if result == range(0,10):
        result.append(i)
        print(result)
