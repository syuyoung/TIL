# 1

word = input('문자열을 입력하세요')

count = 0
for i in word:
    if(i == 'e'):
        count = count + 1
        print(count)


# 2

word = input('문자열을 입력하세요')
count = 0
a = list['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

for i in word:
    if i == a:
        count = count + 1
print(count)

## 정답

string = input("문자열을 입력하세요 > ")
count = 0
for char in string:
    if (
        char == "e"
        or char == "E"
        or char == "a"
        or char == "A"
        or char == "i"
        or char == "I"
        or char == "o"
        or char == "O"
        or char == "u"
        or char == "U"
    ):
        count += 1

print(count)


# 3

dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

dict_variable["나이"] = "24세"

for key, value in dict_variable.items():
    if (key == '나이'):
      print(key, ":", value)


# 4

a = input('이름을 입력하세요 > ')
b = input('전화번호를 입력하세요 > ')
c = input('거주지를 입력하세요 > ')

dict = {
    "이름": a,
    "전화번호": b,
    "거주지": c,
}

print(dict)
for key, value in dict.items():
        print(key, ":", value)


# 5
a = input('이름을 입력하세요 > ')
b = input('전화번호를 입력하세요 > ')
c = input('이메일을 입력하세요 > ')
d = input('거주지를 입력하세요 > ')

dict = {
    a: {
        '전화번호': b,
        '이메일': c,
        '거주지': d
    }
}
print(dict)


# 6
word = input('문자열을 입력하세요 > ')
dict = {}

for a in word:
    if a not in dict:
        dict[a] = '1'

for key, value in dict.items():
    print(key, value)

## 정답

string = input("문자열을 입력하세요 > ")
dict_variable = {}
for char in string:
    if char in dict_variable.keys():
        dict_variable[char] += 1
    elif char not in dict_variable.keys():
        dict_variable[char] = 1

for key, value in dict_variable.items():
    print(key, value)