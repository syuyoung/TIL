T = int(input())

for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    result = []
    for i in numbers:
        if i % 2 == 1:
            result.append(i)
    print(f'#{t} {sum(result)}')