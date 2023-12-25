n=int(input())

arr = list(map(int,input().split()))

max_val = max(arr)

idx1 = arr.index(max_val)

max_val = max(arr[:idx1])

idx2 = arr.index(max_val)

print(idx1+1, idx2+1)