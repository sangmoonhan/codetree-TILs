def f(n):
    if n < 10:
        return n**2

    return f(n // 10) + (n % 10)**2


n = int(input())

print(f(n))