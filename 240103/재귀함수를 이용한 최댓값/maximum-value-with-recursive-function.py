def f(n, arr):
    
    if n == 1:
        if arr[0] > arr[1]:
            return arr[0]
        else :
            return arr[1]
    
    if arr[n-1] > f(n-1,arr) : return arr[n-1]
    else : return f(n-1,arr)

n = int(input())

arr = list(map(int,input().split()))

print(f(n, arr))