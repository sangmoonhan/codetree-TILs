n = int(input())

arr = list(map(int,input().split()))

brr =[]

for i in arr :
    if i % 2 == 0 :
        brr.append(i)

for i in brr[::-1] :
    print(i, end=" ")