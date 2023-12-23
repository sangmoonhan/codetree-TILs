arr = list(map(int, input().split()))

sum_val = sum(arr[1::2])

mean_val = sum(arr[2::3]) / 3

print(int(sum_val), "{:.1f}".format(mean_val))