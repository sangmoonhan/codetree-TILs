arr = input().split()

n = int(arr[0])

ch = arr[1]

cnt = 0

for _ in range(n):

    a = input()

    if a == ch :
        cnt += 1

print(cnt)