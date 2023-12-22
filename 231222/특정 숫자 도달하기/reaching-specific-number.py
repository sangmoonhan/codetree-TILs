arr = list(map(int, input().split()))

sum_val = 0
cnt =0

for i in range(10):
    a = arr[i]

    if a >= 250 :
        break   

    sum_val += a
    cnt += 1

print(sum_val, f"{(sum_val / cnt):.1f}")