n = int(input())

arr = list(map(int,input().split()))

max_val = 0

for i in range(n) :
    for j in arr[(i+1):] :
        if (j - arr[i]) > max_val:
            max_val = j - arr[i]

print(max_val)