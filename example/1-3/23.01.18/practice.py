# #9498

score = int(input())
if score >=90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

# 9093

T = int(input())

for t in range(1, T+1):
    string = input() # 문장 입력
    reverse = string[::-1].split()# 단어 뒤집어 변환 후 분할
    result = reverse[::-1]#분할된 단어 뒤집어 변환
    print(*result)


# 11721

string = input()
string_len = len(string) #길이 지정
for i in range(0, string_len , 10): # 0부터 string 길이까지 반복하는데 10개씩
    print(string[i:i + 10]) #0~10 10개씩 출력

# 2947

input_numbers=list(map(int,input().split()))

numbers = []

for number in input_numbers:
    numbers.append(int(number))
while True:
    for i in range(0, len(numbers) -1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            print(*numbers)
    if numbers == [1, 2, 3, 4, 5]:
        break