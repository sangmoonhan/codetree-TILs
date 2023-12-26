n = int(input())

leng = 0
cnt = 0

for i in range(n) :
    arr = input()

    leng += len(arr)

    if arr[0] == 'a':
        cnt += 1

print(leng, cnt)