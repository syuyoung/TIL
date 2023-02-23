import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = int(input())
    n = int(input())
    price = s

    for i in range(n):
        a,b = map(int,input().split())
        price += a*b
    print(price)