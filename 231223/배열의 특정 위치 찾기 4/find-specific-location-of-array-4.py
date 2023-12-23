arr = list(map(int,input().split()))

cnt = 0

brr=[]

for i in arr :
    if i == 0:
        break
    
    if i % 2 == 0 :
        cnt += 1
        brr.append(i)

print(int(cnt),int(sum(brr)))