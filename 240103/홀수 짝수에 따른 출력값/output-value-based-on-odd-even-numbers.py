def fact(n):
    if n == 2 :
        return 2
    if n == 1 :
        return 1

    return fact(n - 2) + n

n = int(input())

print(fact(n))