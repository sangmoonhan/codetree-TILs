n = int(input())

arr = [ [0 for _ in range(n)] for _ in range(n) ]

num = int(n * n)

for i in range(n):
    if i % 2 == 0 :
        for j in range(n):
            arr[n-1-j][i] = num
            num -= 1
    else :
        for j in range(n):
            arr[j][i] = num
            num -= 1

    
# 출력
for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()