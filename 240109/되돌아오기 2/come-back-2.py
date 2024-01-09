arr = list(input())

x, y = 0, 0

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

cnt = 0

dir_num = 3

for a in arr :

    if a == "L" : 
        dir_num = (dir_num - 1 + 4) % 4
        cnt += 1
        
    elif a == "R" :
        dir_num = (dir_num + 1) % 4
        cnt += 1
        
    else :
        x, y = x + dx[dir_num], y + dy[dir_num]

        cnt += 1
    if x == 0 and y == 0 :
        break

if x == 0 and y == 0 :
    print(cnt)
else :
    print(-1)