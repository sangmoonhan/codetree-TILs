arr = input().split()

a = len(arr[0])

b = len(arr[1])

if a > b :
    print(arr[0],int(a))
elif a < b :
    print(arr[1],int(b))
else :
    print("same")