import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
li = [a,b,c]
sli = sorted(li)
li2 = [d,e]
sli2 = sorted(li2)
print(sli[0]+sli2[0]-50)