import sys
input = sys.stdin.readline

N = int(input())
result = N
for _ in range(N):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            result -= 1
            break
print(result)