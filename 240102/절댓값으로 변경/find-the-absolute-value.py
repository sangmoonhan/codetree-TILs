n = int(input())

arr = list(map(int,input().split()))

def ab(arr):

    brr = arr

    for i in range(len(brr)) :
        if brr[i] < 0 :
            brr[i] *= -1
    
    return brr

brr = ab(arr)

for i in brr:
    print(i,end=" ")