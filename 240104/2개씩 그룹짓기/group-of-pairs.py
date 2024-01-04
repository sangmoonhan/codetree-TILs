n = int(input())

arr = list(map(int,input().split()))

arr.sort()

brr=[]

for i in range(n):

    a = arr[i] + arr[len(arr)-1-i]

    brr.append(a)

print(max(brr))