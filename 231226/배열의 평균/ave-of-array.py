arr = [list(map(int,input().split())) for i in range(2)]

for i in range(2):
    sum_val = 0
    for j in range(4):
        sum_val += arr[i][j]
    
    mean_val = sum_val / 4

    print("{:.1f}".format(mean_val),end=" ")

print()

for j in range(4):
    sum_val = 0
    for i in range(2):
        sum_val += arr[i][j]
    
    mean_val = sum_val / 2

    print("{:.1f}".format(mean_val),end=" ")

print()

sum_val = 0

for i in range(2):
    for j in range(4):
        sum_val += arr[i][j]
    
mean_val = sum_val / 8

print("{:.1f}".format(mean_val),end=" ")