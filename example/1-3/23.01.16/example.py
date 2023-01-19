# 1

A, B =map(int,input().split())
print(A+B)

# 2
A=int(input())
B=int(input())
print(A+B)

# 3
T = int(input())

for t in range(1, T+1):
    A, B =map(int,input().split())
    print(A+B)

# 4

T = int(input())

for t in range(1, T+1):
    A, B =map(int,input().split(','))
    print(A+B)

# 5
T = int(input())

for t in range(1, T+1):
    A, B =map(int,input().split())
    print(f'Case #{t}: {A+B}')

#6
T = int(input())

for t in range(1, T+1):
    A, B =map(int,input().split())
    print(f'Case #{t}: {A} + {B} = {A+B}')