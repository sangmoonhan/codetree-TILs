arr = input().split()

sum_val = 0

for i in arr:

    a = i

    cnt = 0

    for j in a:
        if j.isdigit():
            cnt += 1
        else :
            break
    
    sum_val += int(a[:cnt])

print(sum_val)