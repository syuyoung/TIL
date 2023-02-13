x, y = list(map(str,input().split()))
xy = str(int(x[::-1]) + int(y[::-1]))
print(int(xy[::-1]))