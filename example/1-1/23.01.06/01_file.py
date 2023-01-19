f = open('hello.txt' , 'r', encoding='utf8')
text = f.read()
#text = f.readline() #한줄씩 실행됨
print(text)
f.close()


with open('hello.txt' , 'r', encoding='utf8') as f:
    text = f.readline()
    print(text)
    text = f.readline()
    print(text)
    text = f.readline()
    print(text)