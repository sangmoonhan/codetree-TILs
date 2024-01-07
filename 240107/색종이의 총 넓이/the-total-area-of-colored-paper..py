offset = 100

rect = [[0 for _ in range(201)] for _ in range(201)]

n = int(input())

for _ in range(n):

    x1, y1 = tuple(map(int,input().split()))

    x1 += offset
    y1 += offset
    

    for i in range(x1,x1+8):

        for j in range(y1,y1+8):

            rect[i][j] = 1

sum_val = 0

for i in rect :

    sum_val += sum(i)
    
print(sum_val)