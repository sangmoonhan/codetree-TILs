arr = list(map(int,input().split()))

n, m = arr[0], arr[1]

max_val = 200

arr = [ [0 for _ in range(m)] for _ in range(n) ]

num = 1

for k in range(max_val):
    for l in range(max_val) :
        if 0 <= l <= n-1 and 0 <= k-l <= m-1 : 
            arr[l][k-l] = num
            num+=1

for i in arr:
    for j in i :
        print(j,end=" ")
    print()