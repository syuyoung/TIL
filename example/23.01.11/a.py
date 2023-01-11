a= '#'
b= '+'

result = 0
for i in range(5):
    if i == result:
        print(a, end='')
    else:
        print(b, end='')
print(end='\n')
result = 1
for i in range(5):
    if i == result:
        print(a, end='')
    else:
        print(b, end='')