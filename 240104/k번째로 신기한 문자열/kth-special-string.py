n, k, t = tuple(input().split())

n, k = int(n), int(k)

arr =[]

for i in range(n):

    ch = input()

    if ch[:2] == t :
        arr.append(ch)

arr.sort()

print(arr[k-1])