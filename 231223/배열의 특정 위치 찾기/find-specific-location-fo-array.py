arr = list(map(int, input().split()))

n = len(arr)

sum_val = sum(arr[1::2])

mean_val = sum(arr[2::3]) / 3

print(int(sum_val), mean_val)