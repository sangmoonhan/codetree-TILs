n = int(input())

arr = [ list(input()) for _ in range(n) ]

# 아래 왼 오 위
dx = [1,0,0,-1]
dy = [0,-1,1,0]

start = int(input())

a = start // n
b = start % n

if b == 0 :
    a -= 1

# m * 4
if start <= n :
    x, y, d = 0, start-1, 0 # (b-1 + n)%n

elif start <= 2*n :
    x, y, d = start-n-1, n-1, 1
    
elif start <= 3*n :
    x, y, d = n-1, n-(start-2*n), 2
else : 
    x, y, d = n-(start-3*n), 0, 3

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def f1(x,y,d,m):
    
    if m == "/" : # "/" 의 규칙
        if d == 0 : # ↓ 아래로 오면 ← 왼쪽으로 가고
            a, b = x + dx[1], y + dy[1]
            c = 1
            return a,b,c 
        
        elif d == 1: # ← 왼쪽으로 오면 ↓ 아래로 가고
            a, b = x + dx[0], y + dy[0]
            c = 0
            return a,b,c 

        elif d == 2: # → 오른쪽으로 오면 ↑ 위로 가고
            a, b = x + dx[3], y + dy[3]
            c = 3
            return a,b,c 
        
        elif d == 3: # ↑ 위로 오면 → 오른쪽으로 가고
            a, b = x + dx[2], y + dy[2]
            c = 2
            return a,b,c 
    else : # "\\" "\" 의 규칙
        if d == 0 : # ↓ 아래로 오면 → 오른쪽으로 가고
            a, b = x + dx[2], y + dy[2]
            c = 2
            return a,b,c 
        
        elif d == 2: # → 오른쪽으로 오면 ↓ 아래로 가고
            a, b = x + dx[0], y + dy[0]
            c = 0
            return a,b,c 

        elif d == 1: # ← 왼쪽으로 오면 ↑ 위로 가고
            a, b = x + dx[3], y + dy[3]
            c = 3
            return a,b,c 
        
        elif d == 3: # ↑ 위로 오면 ← 왼쪽으로 가고
            a, b = x + dx[1], y + dy[1]
            c = 1
            return a,b,c
    
    return 2000, 2000, d

#n = int(input())
#arr = [ list(input()) for _ in range(n) ]



brr = [x,y,d]

cnt = 0

while in_range(x,y):

    x,y,d = list(f1(x,y,d,arr[x][y]))

    cnt += 1

print(cnt)

#print(list(f1(brr[0],brr[1],brr[2],arr[brr[0]][brr[1]])))