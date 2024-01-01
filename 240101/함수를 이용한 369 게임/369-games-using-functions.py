def least(n):

    sam=["3","6","9"]

    c = False

    k=list(str(n))

    for i in k:

        if i in sam :
            c = True
            break

    return c

a, b = tuple(map(int,input().split()))

cnt = 0

for i in range(a, b+1):
    if least(i) or (i % 3 == 0) :
        cnt += 1

print(cnt)