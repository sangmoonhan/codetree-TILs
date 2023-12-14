arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

arr = [a,b,c]

m = min(arr)

if a == m :
    x = 1
else :
    x = 0

if a == b and b == c :
    y = 1
else :
    y = 0

print(x,y)