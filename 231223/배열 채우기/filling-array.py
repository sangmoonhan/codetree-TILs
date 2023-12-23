arr = list(map(int, input().split()))

arr1=[]

for i in arr :
    if i == 0 :
        break
    else:
        arr1.append(i)

for i in arr1[::-1]:
    print(i,end=" ")