arr = list(map(int,input().split()))

a1 = sum(arr[::2])
a2 = sum(arr[1::2])

if a1 > a2 :
    print(a1 - a2)
else :
    print(a2 - a1)