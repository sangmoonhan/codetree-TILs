n = int(input())

cnts = []

cnt = 1

for i in range(n):

    a = int(input())

    if i == 0 or b == a :
        cnt += 1
    else:
        cnts.append(cnt)
        cnt = 1
    
    if i == n-1:
        cnts.append(cnt)
    
    b = a

print(max(cnts))