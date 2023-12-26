n = int(input())

arr_2d = [ [0 for _ in range(n)]  for _ in range(n) ]

# 1. 첫 번째 행에 전부 숫자 1을 채웁니다.
for i in range(n):
    arr_2d[i][i] = 1
    arr_2d[i][0] = 1

# 2. 두 번째 행부터 마지막 행까지 전부 숫자를 채웁니다.
for i in range(2, n):
    for j in range(1,i):
        arr_2d[i][j] = arr_2d[i - 1][j-1] + arr_2d[i-1][j]

# 출력
for i in range(1,n+1):
    for j in range(i):
        print(arr_2d[i-1][j], end=" ")
    print()