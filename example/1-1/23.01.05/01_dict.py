# 전화번호부
# 키 - 이름(상호명)
# 값 - 전화번호
phone_book = {
    '피자헛': '1588-5588', # 숫자로 구성된 문자열
    '전화번호': '114',
    '서유영': '010-1234-1234',
    '대리운전': '1577-1577'
}

print(phone_book['피자헛'])

for name in phone_book:
    # 키 순회
    print(name)
    # 값 순회    
    print(phone_book[name])


#for ..  특정 변수의 이름

string = 'hello'
dict_variable = {}

for char in string:
    print(char)
    if char in dict_variable: