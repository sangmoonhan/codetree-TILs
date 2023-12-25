n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr[0], arr[1])
second_max_val = min(arr[0], arr[1])

for i in range(2, n):
    if arr[i] > max_val:
        second_max_val = max_val
        max_val = arr[i]
    elif arr[i] > second_max_val:
        second_max_val = arr[i]

print(max_val, second_max_val)