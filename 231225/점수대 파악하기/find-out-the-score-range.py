arr = list(map(int,input().split()))

cnt = [0] * 11

for i in arr :
    if i == 0 :
        break
    
    cnt[i // 10] += 1

cnt=cnt[::-1]

cnt.pop()

for i in range(10):
    print("{} - {}".format(int(100 - 10 * i),cnt[i]))