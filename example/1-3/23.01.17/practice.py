# 9085

T = int(input())

for t in range(1, T+1):
    N = input()
    numbers = list(map(int,input().split()))
    print(sum(numbers))

# 10824

a,b,c,d = map(str,input().split())
ab = int(a+b)
cd = int(c+d)
print(ab+cd)

# 3009

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4 = 0
y4 = 0
if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1

if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1

print(x4,y4)

# 10952
while True:
    a, b = map(int,input().split())
    if a+b > 0:
        print(a+b)
    else:
        break

# 1110
n = input()
i = n
if int(i) < 10:
    i= '0' + i
cnt = 0
while True:

    first = i[-1]
    second = i[0]
    sum_number = int(first) + int(second)
    new_number = i[-1] + str(sum_number)[-1]
    cnt += 1
    if int(new_number) == int(n):
        break
    i = new_number

print(cnt)