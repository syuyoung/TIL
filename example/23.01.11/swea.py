# 1

string = input().upper().split()
print(*string)


# 2

number = int(input())
print(sum(range(1,number+1)))


# 3

a, b = list(map(int,input().split()))

if a == 1 and b == 2:
    print('B')
elif a == 1 and b == 3:
    print('A')
elif a == 2 and b == 1:
    print('A')
elif a == 2 and b == 3:
    print('B')
elif a == 3 and b == 1:
    print('B')
elif a == 3 and b == 2:
    print('A')


# 4

print('#++++')
print('+#+++')
print('++#++')
print('+++#+')
print('++++#')


# 5

number = int(input())
a = sum(map(int, str(number)))
print(a)


# 6

number = int(input())

for i in range(number+1):
    print(2**i, end=' ')