n = int(input())

arr = list(map(int,input().split()))

arr = [arr[i] for i in range(n) if arr[i] % 2 == 0 ]

for i in arr:
    print(i, end=" ")