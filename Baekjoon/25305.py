import sys
input = sys.stdin.readline

N, k = list(map(int,input().split()))
numbers = list(map(int,input().split()))
s_numbers = sorted(numbers, reverse=True)
print(s_numbers[k-1])