offset = 1000

rect = [[0 for _ in range(2001)] for _ in range(2001)]

for _ in range(2):

    x1, y1, x2, y2 = tuple(map(int,input().split()))

    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset

    for i in range(x1,x2):

        for j in range(y1,y2):

            rect[i][j] = 1

for _ in range(1):

    x1, y1, x2, y2 = tuple(map(int,input().split()))

    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset

    for i in range(x1,x2):

        for j in range(y1,y2):

            rect[i][j] = 0

sum_val = 0

for i in rect :

    sum_val += sum(i)
    
print(sum_val)