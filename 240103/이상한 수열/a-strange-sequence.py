def f(n):
    # 종료 조건
    if n == 1:
        return 1
    if n == 2:
        return 2

    # 점화식
    return f(n//3 ) +  f(n - 1)

n = int(input())

print(f(n))