arr=input().split()
a = int(arr[0])
b = int(arr[1])

if a < b:
    print(b-a)

if b < a:
    print(a-b)

if a==b:
    print(0)