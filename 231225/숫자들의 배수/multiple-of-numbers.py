n = int(input())

print(n,end=" ")

arr = [n]

cnt = 0
while True :
    if arr[-1] % 5 == 0 :
        cnt += 1
    if cnt == 2:
        break
    
    arr.append(arr[0]+arr[-1])

    print(arr[-1], end=" ")