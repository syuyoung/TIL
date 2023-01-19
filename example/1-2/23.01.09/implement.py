# 1

string = input('문자열을 입력하세요 > ')
count = 0

for word in string:
    if 'e' in word:
        print(count)
    else:
        count += 1
        if count == len(string):
            print(-1)


2


string = list(map(str,input('문자열을 입력하세요 > ').split()))

count = 0
for word in string:
    count = count + 1
    print(word, count)
    

# 3

string = input('문자열을 입력하세요 > ')

result = ()
for word in string:
    if 'e' not in word:
        result = word
        print(result,end ='')


# 4

a, b = list(map(str,input('문자열을 입력하세요 > ').split()))

count = 0
for word in a:
    if b == word:
        count += 1
print(count)


# 5

a, b, c = list(map(str,input('문자열을 입력하세요 > ').split()))

print(a+'-'+b+'-'+c)


# 6

numbers = input()
num_list = []
if int(numbers) > 0:
    for num in range(len(numbers)):
        num_list.append(int(numbers[num]))
    print(sum(num_list))
else:
    print(-1)