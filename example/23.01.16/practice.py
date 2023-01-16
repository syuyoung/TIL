# 1
name1 = int(input())
name2 = int(input())
name3 = int(input())
name4 = int(input())
name5 = int(input())
list = [name1, name2, name3, name4, name5]
fix_list = []
for i in list:
    if i < 40:
        fix_list.append(40)
    else :
        fix_list.append(i)
avg = sum(fix_list) / len(fix_list)
print(round(avg))


# 2

N, X = list(map(int,input().split()))
numbers = list(map(int,input().split()))
list = []
for i in numbers:
    if i < X:
        list.append(i)
print(*list)


# 3

a, b, c = list(map(int,input().split()))
list = []
if a == b == c:
    list = 10000+a*1000
elif a == b:
    list = 1000+a*100
elif b == c:
    list = 1000+b*100
elif a == c:
    list = 1000+c*100
else:
    list = [a,b,c]
    list = sorted(list)
    list = list[2]*100

print(list)


# 4

T = int(input())
result = 0
for t in range(1, T+1):
    N = int(input())

    for i in range(N):
        result += N
if result > T//2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')

5

N=int(input())
numbers = list(map(int,input().split()))
point = 0
result = 0
for i in range(N):
    if numbers[i] == 1:
        point += 1
        result += point
    else:
        point = 0
print(result)