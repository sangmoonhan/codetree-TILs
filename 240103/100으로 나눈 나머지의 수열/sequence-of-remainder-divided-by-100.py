def f(n):
    # 종료 조건
    if n == 1:
        return 2
    if n == 2:
        return 4

    # 점화식
    return (f(n - 1) *  f(n - 2)) % 100

n = int(input())

print(f(n))