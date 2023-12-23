arr = list(map(int, input().split()))

brr = []

for i in arr :
    if i == 0 :
        break

    brr.append(i)

sum_val = 0

for i in range(1,4) :
    sum_val += brr[-i]

print(sum_val)