arr = input().split()

a = ord(arr[0])
b = ord(arr[1])

if a > b :
    print(a+b,a-b)
else :
    print(a+b,b-a)