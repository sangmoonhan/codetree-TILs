n = int(input())
arr = list(map(float, input().split()))

sum_val = sum(arr)

mean_val = sum_val / n

print("{:.1f}".format(mean_val))

if mean_val >= 4 :
    print("Perfect")
elif mean_val >= 3 :
    print("Good")
else :
    print("Poor")