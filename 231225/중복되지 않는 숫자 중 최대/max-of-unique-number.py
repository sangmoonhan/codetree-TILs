n = int(input())

arr = list(map(int,input().split()))

max_val = -1

for i in arr :
    if arr.count(i) == 1 :
        if max_val < i :
            max_val = i

print(max_val)