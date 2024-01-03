'''
max( f(1), f(2), f(3), f(4), f(5), f(6) )
= max( max( max(f(1), f(2)) , f(3) ), f(4), f(5), f(6) )
'''

def f(n, arr):
    
    if n == 1:
        if arr[0] > arr[1]:
            return arr[0]
        else :
            return arr[1]
    
    if arr[n-1] > f(n-1,arr)  :
        return arr[n-1]
    else : 
        return f(n-1,arr)

n = int(input())

arr = list(map(int,input().split()))

print(f(n, arr))