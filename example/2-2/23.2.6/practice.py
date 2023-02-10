#10769

word = input()
happy = word.count(':-)')
sad = word.count(':-(')


if happy == 0 and sad == 0:
    print('none')
elif happy == sad:
    print('unsure')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')


import sys


people = []
result = 0

for _ in range(4):
    a, b = map(int,sys.stdin.readline().split())
    result += b
    result -= a

    people.append(result)

print(max(people))