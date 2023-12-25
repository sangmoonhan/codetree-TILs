n = int(input())

arr = list(map(int,input().split()))

cnt = 0
cnt2 = 0
for i in arr:
    if i == 2 :
        cnt2 += 1

    if cnt2 == 3:
        print(cnt + 1 )
        break

    cnt += 1