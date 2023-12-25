arr = list(map(int,input().split()))

cnt = [0] * 6


for i in arr :
    cnt[i-1] += 1

for i in range(1,7):
    print("{} - {}".format(i,cnt[i-1]))