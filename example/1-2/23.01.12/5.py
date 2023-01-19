
T = int(input())

for x in range(1, T+1):
    num = int(input())
    count = 0
    result = []
    for i in range(num):
        result= i*count+1
    if result == range(0,10):
        result.append(i)
        print(result)
