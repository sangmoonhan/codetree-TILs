arr = list(map(float, input().split()))

sum_val=0
cnt=0

for i in arr :
    if i == 0 :
        break
    sum_val +=i
    cnt += 1

print(int(sum_val),"{:.1f}".format(sum_val / cnt))