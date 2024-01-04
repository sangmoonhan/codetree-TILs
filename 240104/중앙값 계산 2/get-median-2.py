n = int(input())

arr = list(map(int,input().split()))

for i in range(n) : 

    a = arr[i]

    if i % 2 == 0 :

        brr = arr[:i+1]

        brr.sort()

        print(brr[i//2],end=" ")