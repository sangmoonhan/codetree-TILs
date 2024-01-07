offset = 100

rect = [[0 for _ in range(201)] for _ in range(201)]

n = int(input())

for k in range(n):

    x1, y1, x2, y2 = tuple(map(int,input().split()))

    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset

    if k % 2 == 0 :
        
        for i in range(x1,x2):
            
            for j in range(y1,y2):
                
                rect[i][j] = 1
    else :
        
        for i in range(x1,x2):
            
            for j in range(y1,y2):
                
                rect[i][j] = 2

sum_val = 0

for i in rect :
    for j in i :
        if j == 2 :
            sum_val += 1
    
print(sum_val)