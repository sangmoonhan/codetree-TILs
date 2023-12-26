n = int(input())

arr_2d = [ [0 for _ in range(n)]  for _ in range(n) ]

for i in range(n):
    arr_2d[0][i] = 1
    arr_2d[i][0] = 1

# 2. 두 번째 행부터 마지막 행까지 전부 숫자를 채웁니다.
for i in range(1, n):
    for j in range(1,n):
        arr_2d[i][j] = arr_2d[i - 1][j-1] + arr_2d[i-1][j] + arr_2d[i][j-1]

# 출력
for i in arr_2d:
    for j in i:
        print(j, end=" ")
    print()