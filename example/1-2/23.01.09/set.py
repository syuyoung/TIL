my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
list = []
for num in my_list:
    if num not in list:
        list.append(num)

print(list)
print(len(list))
print(set(my_list))

print(len(set(my_list)))