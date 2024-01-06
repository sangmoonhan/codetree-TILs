a,b,c = tuple(map(int,input().split()))

d = 11
h = 11
m = 11

elapsed_mins = 0

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if a < 11 :
    print(-1)
elif a == 11 :
    if h < 11 :
        print(-1)
    elif h == 11 :
        if m < 11:
            print(-1)
else :
    while True:
        if d == a and h == b and m == c:
            break

        elapsed_mins += 1
        m += 1

        if m == 60 :
            h += 1
            m = 0
    
        if h == 24 :
            d += 1
            h = 0

    print(elapsed_mins)