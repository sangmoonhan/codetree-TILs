def power(n,m):
    num = 1 

    for _ in range(m):
        num *= n
    
    return num

n, m = tuple(map(int,input().split()))


print(power(n,m))