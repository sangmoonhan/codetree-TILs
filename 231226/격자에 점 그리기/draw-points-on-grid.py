arr = list(map(int,input().split()))

n, m = arr[0], arr[1]

arr = [ [ 0 for _ in range(n) ] for _ in range(n) ]

num=1

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    
    arr[r-1][c-1] = num

    num += 1


for i in arr :
    for j in i :
        print(j,end=" ")
    print()