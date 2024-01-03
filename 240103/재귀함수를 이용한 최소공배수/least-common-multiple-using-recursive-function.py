n = int(input())

arr = list(map(int,input().split()))

def f(n,arr) :
    if n == 0 :
        return arr[0]

    c = f(n-1,arr)
    gcd1 = 1
    
    for j in range(1, min(c,arr[n-1]) + 1):
        
        if c % j == 0 and arr[n-1] % j == 0 :
            gcd1=j

    return c * arr[n-1] // gcd1

print(f(n,arr))