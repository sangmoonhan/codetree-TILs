n = 8
arr = list(map(float, input().split()))

sum_val = sum(arr)

mean_val = sum_val / n

print("{:.1f}".format(mean_val))