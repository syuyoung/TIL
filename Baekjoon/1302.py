N = int(input())
li = {}
for _ in range(N):
    book = input()

    if book in li.keys():
        li[book] += 1
    else:
        li[book] = 1

max_value = max(li.values())

best = []
for key, value in li.items():
    if value == max_value:
        best.append(key)

best = sorted(best)
print(best[0])