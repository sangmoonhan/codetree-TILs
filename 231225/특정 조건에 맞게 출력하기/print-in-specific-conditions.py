arr = list(map(int,input().split()))

brr = []

for i in arr :
    if i == 0 :
        break
    
    brr.append(i)

for i in brr :
    if i % 2 == 1 :
        print(i+3, end=" ")
    else :
        print(i//2, end=" ")