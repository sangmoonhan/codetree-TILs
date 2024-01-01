def least(n):

    sam=[3,6,9]

    if n >= 10 :
        a = n // 10
        b = n % 10

        c = ( a in sam ) or ( b in sam ) or (n % 3 == 0)
    else :
        c = ( n in sam ) or (n % 3 == 0)

    return c


a, b = tuple(map(int,input().split()))

cnt = 0
for i in range(a, b+1):
    if least(i):
        cnt += 1

print(cnt)