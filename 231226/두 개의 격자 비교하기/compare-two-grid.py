arr = list(map(int,input().split()))

n, m = arr[0], arr[1]

arr = [ list(map(int,input().split())) for i in range(n)]

brr = [ list(map(int,input().split())) for i in range(n)]

crr = [ [1 for j in range(m) ] for i in range(n)]

for i in range(n):

    for j in range(m):
        if arr[i][j] == brr[i][j]:
            crr[i][j] = 0

        print(crr[i][j], end=" ")

    print()