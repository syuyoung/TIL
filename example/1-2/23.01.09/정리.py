numbers = input()
num_list = []
if int(numbers) > 0:
    for num in range(len(numbers)):
        num_list.append(int(numbers[num]))
    print(sum(num_list))
else:
    print(-1)