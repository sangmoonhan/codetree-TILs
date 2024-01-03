def f(cnt,n):
    if n == 1:
        return cnt

    if n % 2 == 0:
        cnt += 1
        return f(cnt ,n // 2)
    else:
        cnt += 1
        return f(cnt, n * 3 + 1)

n = int(input())

print(f(0,n))