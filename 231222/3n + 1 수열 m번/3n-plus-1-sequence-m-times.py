n = int(input())

for i in range(n):
    m = int(input())

    cnt=0

    while m != 1 :
        if m % 2 == 0 :
            m = m//2
            cnt += 1
        else :
            m  = 3*m + 1
            cnt += 1
    
    print(cnt)