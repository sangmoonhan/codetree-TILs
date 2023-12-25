n = int(input())

arr = [1, n]

print(arr[0],end=" ")
print(arr[1],end=" ")

while True :
    arr.append(arr[-1] + arr[-2])

    print(arr[-1], end=" ")

    
    if arr[-1] > 100 :
        break