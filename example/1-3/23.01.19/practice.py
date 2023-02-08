# # # 2576

# list = [int(input()) for _ in range(7)]
# odd = []
# even = []

# for i in list:
#     if (i) % 2 ==1:
#         odd.append(i)
#     elif (i) % 2 == 0:
#         even.append(i)
# if len(odd) != 0:
#     print(sum(odd))
#     print(min(odd))
# else:
#     print('-1')

# # 10822

# numbers = list(map(int,input().split(',')))
# print(sum(numbers))

# # 2754

# score = {'A+': '4.3', 'A0': '4.0', 'A-': '3.7',
# 'B+': '3.3', 'B0': '3.0', 'B-': '2.7',
# 'C+': '2.3', 'C0': '2.0', 'C-': '1.7',
# 'D+': '1.3', 'D0': '1.0', 'D-': '0.7', 'F' : '0.0'
# }
# print(score[input()])


# 5622
word = input()
dial =['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0
for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            time += dial.index(j) + 3
print(time)


# # 2577

# list = [int(input()) for _ in range(3)]
# result = str(list[0]*list[1]*list[2])
# for i in range(10):
#     print(result.count(str(i)))

# # 7785

# import sys
# n = int(sys.stdin.readline())
# data = {sys.stdin.readline().strip().split() for i in range(n)}
# print(data)
# list = []
# for i in data:
#     if i in 'enter':
#         list.append(i)


# print(list)