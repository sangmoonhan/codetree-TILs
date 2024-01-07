m1, d1, m2, d2 = tuple(map(int,input().split()))

idx = 1

yoil = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m1 == m2 :
        
    idx = idx + int(d2-d1)
        
    idx = idx % 7

    print(yoil[idx])
elif m1 < m2 : 
    
    month, day = m1, d1
    
    while True:
        if month == m2 and day == d2:
            break

        idx += 1
        day += 1

        if day > num_of_days[month]:
            month += 1
            day = 1
    
    idx = idx % 7

    print(yoil[idx])
else :

    month, day = m2, d2
    
    while True:
        if month == m1 and day == d1:
            break

        idx -= 1
        day += 1

        if day > num_of_days[month]:
            month += 1
            day = 1
    
    idx = idx % 7

    print(yoil[idx])