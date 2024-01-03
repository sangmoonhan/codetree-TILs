n = int(input())

arr = list(map(int,input().split()))

val = arr[0]

for i in arr[1:] :
    for j in range(1, int(val * i) + 1):
        if j % val == 0 and j % i == 0 :
            val = j
            break

print(val)