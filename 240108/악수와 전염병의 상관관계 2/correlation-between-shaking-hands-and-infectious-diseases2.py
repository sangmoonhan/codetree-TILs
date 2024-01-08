n, k, p, T = tuple(map(int,input().split()))

cnts = [k] * (n+1)


infected = [0] * (n+1)
infected[p] = 1

arr = []

for i in range(T):

    arr.append(tuple(map(int,input().split())))

arr.sort(key=lambda x: x[0])

for i in range(T):

    t, x, y = arr[i]

    if infected[x] == 1 and infected[y] == 0 :
        if cnts[x] > 0 :
            infected[y] = 1
            #cnts[y] = k
            cnts[x] -= 1
            continue
    elif infected[y] == 1 and infected[x] == 0 :
        if cnts[y] > 0 :
            infected[x] = 1
            #cnts[x] = k
            cnts[y] -= 1

for i in range(1,len(infected)):
    print(infected[i],end="")