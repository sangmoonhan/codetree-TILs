x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

n = int(input())

for _ in range(n):

    d, t = input().split()

    t = int(t)

    if d == "E" : 
        d = 0
    elif d == "S" :
        d = 1
    elif d == "W" :
        d = 2
    else :
        d = 3

    x, y = x + int(t * dx[d]), y + int(t * dy[d])

print(x,y)