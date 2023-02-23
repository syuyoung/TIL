import sys
input = sys.stdin.readline

a, b = map(int,input().split())

list_a = set(map(int,input().split()))
list_b = set(map(int,input().split()))

result = list_a-list_b 
s_result = sorted(result)

print(len(s_result))
print(*s_result)