def add(n):

    ls = []

    for i in range(1,n+1):
        ls.append(i)

    return ( sum(ls) // 10 )


n = int(input())

print(add(n))