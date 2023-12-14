arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if (a <= b <= c) or (c <= b <= a) :
    print(b)
elif (b <= a <= c) or (c <= a <= b) :
    print(a)
else :
    print(c)