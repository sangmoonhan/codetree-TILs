n = int(input())

a = [ list(map(int,input().split())) for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

sum_val = 0

for i in range(n):
    for j in range(n):

        cnt = 0

        x, y = i,j

        for dx, dy in zip(dxs, dys):
            
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny) and a[nx][ny] == 1:
                
                cnt += 1
        
        if cnt >= 3 :
            sum_val += 1

print(sum_val)