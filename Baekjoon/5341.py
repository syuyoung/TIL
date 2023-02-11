import sys
input = sys.stdin.readline

while True:
    a = int(input())
    if a == 0:
        break
    result = 0
    for i in range(1,a+1):
        result += i
    
    print(result)