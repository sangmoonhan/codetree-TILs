sum_val = 0
cnt = 0
for i in range(10):
    a = int(input())

    if 0 <= a <= 200:
        sum_val += a
        cnt += 1

mean_val = sum_val / cnt

print(sum_val, "{:.1f}".format(mean_val))