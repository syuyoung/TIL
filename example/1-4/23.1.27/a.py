import sys

input = sys.stdin.readline

T = int(input())
for i in range(1, T+1):
    numbers = list(map(int,input().split()))
    s_num=sum(numbers[1:])/len(numbers[1:])
    sum_list = []
    for i in numbers:
        if i > s_num:
            sum_list.append(i)

print(f'{len(sum_list)/len(numbers[1:])*100:.3f}%')