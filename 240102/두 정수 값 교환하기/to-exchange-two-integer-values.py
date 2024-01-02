a, b = tuple(map(int,input().split()))

def change(n,m):

    n, m = m, n

    return n, m

a, b = change(a,b)

print(a,b)