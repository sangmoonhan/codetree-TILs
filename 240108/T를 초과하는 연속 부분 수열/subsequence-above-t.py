n, t = tuple(map(int,input().split()))

arr = list(map(int,input().split()))

cnts = []

cnt = 0

for i in range(n):

    a = arr[i]

    if t < a :
        cnt += 1
    else:
        cnts.append(cnt)
        cnt = 0
    
    if i == n-1:
        cnts.append(cnt)
    

print(max(cnts))