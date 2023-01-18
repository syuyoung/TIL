#2789
word = list(input())
block = ['C','A','M','B','R','I','D','G','E']
result = []
for i in word:
    if i not in block:
        result.append(i)
print(''.join(result))

# 2675

T = int(input())

for t in range(1, T+1):
    R, S = input().split()
    for i in S:
        print(i*int(R), end='')
    print()


# 10988

word = list(input())
r_word = word[::-1]
if word == r_word:
    print(1)
else:
    print(0)


# 17249

L,R = input().split("(^0^)")
print(L.count('@'),R.count('@'))


# 2941

word = input()
list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in list:
    word = word.replace(i, 'a')
print(len(word))

# 10809
