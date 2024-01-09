x, y = 0, 0           # 시작은 (0, 0) 입니다.

mapper = {
    'E': 0,
    'S': 1,
    'N': 2,
    'W': 3
}

### d =    [0, 1, 2,  3]  [오, 아, 왼, 위]
dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]

n = int(input())

cnt = 0

for _ in range(n):

    d, t = tuple(input().split())

    t = int(t)

    for _ in range(t) : 

        x, y = x + dxs[mapper[d]], y + dys[mapper[d]]

        cnt += 1

        if x == 0 and y == 0 :
            break
    
    if x == 0 and y == 0 :
            break

if x == 0 and y == 0 :
    print(cnt)
else :
    print(-1)