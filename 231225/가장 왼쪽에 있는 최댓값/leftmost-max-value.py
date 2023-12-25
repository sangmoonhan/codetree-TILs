n=int(input())

arr = list(map(int,input().split()))

idx = n+1

while idx != 0 :
    max_val = max(arr[:idx])

    idx = arr.index(max_val)

    print(idx+1, end=" ")