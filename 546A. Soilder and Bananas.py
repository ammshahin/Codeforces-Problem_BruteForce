k, n, w = map(int, input().split())
cost = k
for i in range(1,w):
    cost += (i+1)*k
if cost > n:
    print(cost-n)
else:
    print('0')
