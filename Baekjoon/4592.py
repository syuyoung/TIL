import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
while True:
    li = []
    arr = ''
    number = input().split()
    if number[0] == '0':
        break
    for i in number:
        if i not in li:
            li.append(i)
        elif i in li:
            if li[-1] != i:
                li.append(i)
    print(*li[1::], '$')