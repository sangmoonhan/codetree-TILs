n = int(input())

arr = [ 0 for _ in range(101)]

for i in range(n):

    x1, x2 = tuple(map(int,input().split()))

    for j in range(x1,x2+1):

        arr[j] += 1

print(max(arr))