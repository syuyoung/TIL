import sys
input = sys.stdin.readline

while True:
    a, b = list(map(int,input().split()))
    if a == 0 and b == 0:
        break
    if b%a == 0:
        print('factor')
    elif a%b == 0:
        print('multiple')
    elif b%a and a%b != 0:
        print('neither')