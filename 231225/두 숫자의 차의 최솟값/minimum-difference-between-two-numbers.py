n = int(input())

arr = list(map(int,input().split()))

min_val = max(arr)

for i in arr:
    for j in arr:
        if i < j :
            if j-i < min_val :
                min_val = j-i

print(min_val)