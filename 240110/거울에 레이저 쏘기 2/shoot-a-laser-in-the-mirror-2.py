n = int(input())
arr = [ list(input()) for _ in range(n) ]

# 아래 왼 오 위
dx = [1,0,0,-1]
dy = [0,-1,1,0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# "/" 의 규칙

# "\" 의 규칙

def f1(x,y,d,m):
    
    if m == "/" :
        if in_range(x + dx[1], y + dy[1]) and d == 0 : # ↓ 아래로 오면 ← 왼쪽으로 가고
            a, b = x + dx[1], y + dy[1]
            c = 1
            return a,b,c 
        
        elif in_range(x + dx[0], y + dy[0]) and d == 1: # ← 왼쪽으로 오면 ↓ 아래로 가고
            a, b = x + dx[0], y + dy[0]
            c = 0
            return a,b,c 

        elif in_range(x + dx[3], y + dy[3]) and d == 2: # → 오른쪽으로 오면 ↑ 위로 가고
            a, b = x + dx[3], y + dy[3]
            c = 3
            return a,b,c 
        
        elif in_range(x + dx[2], y + dy[2]) and d == 3: # ↑ 위로 오면 → 오른쪽으로 가고
            a, b = x + dx[2], y + dy[2]
            c = 2
            return a,b,c 
    else : # "\\"
        if in_range(x + dx[2], y + dy[2]) and d == 0 : # ↓ 아래로 오면 → 오른쪽으로 가고
            a, b = x + dx[2], y + dy[2]
            c = 2
            return a,b,c 
        
        elif in_range(x + dx[0], y + dy[0]) and d == 2: # → 오른쪽으로 오면 ↓ 아래로 가고
            a, b = x + dx[0], y + dy[0]
            c = 0
            return a,b,c 

        elif in_range(x + dx[3], y + dy[3]) and d == 1: # ← 왼쪽으로 오면 ↑ 위로 가고
            a, b = x + dx[3], y + dy[3]
            c = 3
            return a,b,c 
        
        elif in_range(x + dx[1], y + dy[1]) and d == 3: # ↑ 위로 오면 ← 왼쪽으로 가고
            a, b = x + dx[1], y + dy[1]
            c = 1
            return a,b,c
    
    return n, n, d

#n = int(input())
#arr = [ list(input()) for _ in range(n) ]

start = int(input())

a = start // n
b = start % n

# m * 4
if a == 0 :
    x, y = 0, (b-1 + n)%n
    d = 0
elif a == 1 :
    x, y = (b-1 + n)%n, n-1
    d = 1
elif a == 2:
    x, y = n-1, (b-1 + n)%n 
    d = 3
else : 
    x, y = (b-1 + n)%n, 0 
    d = 2

brr = [x,y,d]

cnt = 0

while in_range(x,y):

    x,y,d = list(f1(x,y,d,arr[x][y]))

    cnt += 1

print(cnt)

#print(list(f1(brr[0],brr[1],brr[2],arr[brr[0]][brr[1]])))