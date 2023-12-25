arr = list(map(int,input().split()))

n = arr[0]
q = arr[1]

arr = list(map(int,input().split()))

for _ in range(q):

    brr = list(map(int,input().split()))

    if brr[0] == 1:

        print(arr[brr[1] - 1])

    elif brr[0] == 2:

        if brr[1] in arr :
            cnt = 0
            for i in arr :

                if i == brr[1]:
                    print(cnt+1)
                    break
                
                cnt += 1
        else :
            print(0)

    else :
        for i in arr[brr[1]-1:brr[2]]:
            print(i, end=" ")