
string = list(map(str,input('문자열을 입력하세요 > ').split()))

count = 0
for n in string:
    if word in n:
        count = count + 1
    print(n, count)