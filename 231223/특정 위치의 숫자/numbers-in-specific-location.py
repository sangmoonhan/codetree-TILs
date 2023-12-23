arr = list(map(int,input().split()))
n = len(arr)

sum_val = 0

for i in range(n):
    if i == 2 or i == 4 or i == 9 :
        sum_val += arr[i]

print(sum_val)