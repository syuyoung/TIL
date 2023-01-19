a = input()
print(a) # '2 5'
# 원하는 것은 숫자 2와 숫자 5

# 1. 문자열을 각각 쪼갠 요소를 가진 리스트로 변환 - >  .split()
b = a.split()

# 2. 각 요소를 숫자로 변환
print(b)
c = map(int, b)
print(c) # map 

# 3. 각각 변수에 저장
d, e = list(c)[2, 5]
print(d, e) # 각각 2, 5