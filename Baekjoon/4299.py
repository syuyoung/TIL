import sys
input = sys.stdin.readline

a, b = map(int,input().split())
if (a+b)%2==1 or b>a: print(-1)
else: print((a+b)//2, (a-b)//2)