def f(n):
    if n < 10:
        return n

    return f(n // 10) + (n % 10)


def g(n,arr) :
    if n == 0 :
        return 1

    return g(n-1, arr) * arr[n-1]

arr = list(map(int,input().split()))

n=3

print(f(g(n,arr)))