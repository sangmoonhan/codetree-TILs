sum_val = 0
cnt = 0
while True :
    
    a = int(input())
    
    if a <= 19 or a >= 30 :
        break

    sum_val += a
    cnt += 1

print("{:.2f}".format(sum_val / cnt))