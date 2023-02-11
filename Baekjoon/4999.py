import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

a = input()
b = input()

if b in a:
    print('go')
else:
    print('no')