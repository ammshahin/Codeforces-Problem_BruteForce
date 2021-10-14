n = int(input())
final = 0
for _ in range(n):
    pb = list(map(int, input().split()))
    count = 0
    for i in pb:
        if i == 1:
            count += 1
    if count >= 2:
        final += 1
print(final)
