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