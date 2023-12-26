arr = list(map(int,input().split()))

n, m = arr[0],arr[1]

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num=1

for i in range(n):
    for j in range(m):
        arr[i][j] = num
        num += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    
    print()