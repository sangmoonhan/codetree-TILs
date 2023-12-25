arr = list(map(int,input().split()))

for i in range(10):
    print(arr[i],end=" ")

    arr.append(arr[-1]+2*arr[-2])