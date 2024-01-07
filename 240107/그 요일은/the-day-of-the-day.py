m1, d1, m2, d2 = tuple(map(int,input().split()))

ch = input()

idx = 1

yoil = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, day = m1, d1

cnt = 0

while True:

    if yoil[idx % 7] == ch :
        cnt += 1

    if month == m2 and day == d2:
        break

    idx += 1
    day += 1

    if day > num_of_days[month]:
        month += 1
        day = 1

print(cnt)