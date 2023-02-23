import sys

input = sys.stdin.readline
result = 0
score = 0
for _ in range(10):
    n = int(input())
    score += n
    if 100-result >= abs(100-score):
        result = score
print(result)