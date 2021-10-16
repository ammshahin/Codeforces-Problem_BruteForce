arr = []
for i in range(5):
    ele = list(map(int,input().split()))
    arr.append(ele)

_x = 0
_y = 0
for x in arr:
    for y in x:
        if y == 1:
            _x = arr.index(x)
            _y = x.index(y)

if _x <= 2:
    p = 2 - _x
else:
    p = _x - 2
if _y <= 2:
    q = 2 - _y
else:
    q = _y - 2
print(p + q)
