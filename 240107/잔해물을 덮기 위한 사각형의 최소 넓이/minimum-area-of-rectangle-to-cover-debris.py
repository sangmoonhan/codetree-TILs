square1 = list(map(int, input().split()))
square2 = list(map(int, input().split()))

# x1, y1, x2, y2
# 0 1 2 3

offset = 1000
max_r = 2000

grid = [
    [0]*(max_r+1)
    for i in range(max_r+1)
]

# print(grid)

x1, y1, x2, y2 = map(lambda x: x+offset, square1)

# print(x1, y1, x2, y2 )

for i in range(x1, x2): 
    for j in range(y1, y2):
        grid[i][j] = 1
    

x1, y1, x2, y2 = map(lambda x: x+offset, square2)

for i in range(x1, x2): 
    for j in range(y1, y2):
        grid[i][j] = 0

# 조건에 맞지 않는다면 
# 즉 겹치지 않는다면 전부 0이기 때문에 갱신이 되지 않을 것이다 
min_x = max_r
min_y = max_r
max_x = 0
max_y = 0

# 1인 경우 x,y의 최대 좌표와  최소 좌표를 구해보자
for i in range(max_r+1):
    for j in range(max_r+1):
        if grid[i][j] == 1:
            max_x = max(max_x, i)
            max_y = max(max_y, j)
            min_x = min(min_x, i)
            min_y = min(min_y, j)

area = 0

if min_x == max_r and min_y == max_r and max_x == 0 and max_y == 0 :
    area = 0
else :
    area = (max_x-min_x+1) * (max_y- min_y+1)

print(area)