import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a, b = map(int,input().split())

list_a = set(map(int,input().split()))
list_b = set(map(int,input().split()))
print(list_a)
print(list_b)
result = list_a-list_b 
print(result)
s_result = sorted(result)
print(len(s_result))
print(*s_result)