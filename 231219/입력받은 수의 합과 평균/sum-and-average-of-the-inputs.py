n = int(input())

sum_val=0

for i in range(n):
    a = int(input())
    
    sum_val += a

mean_val = sum_val / n

print(sum_val, "{:.1f}".format(mean_val))