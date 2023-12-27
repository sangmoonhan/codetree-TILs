n = int(input())

cnt = 0

sum_val = 0

arr = []

for i in range(n):
    a = input()

    arr.append(a)

ch=input()

for i in arr :
    if ch == i[0] :
        sum_val += len(i)
        cnt += 1

print(cnt,"{:.2f}".format(sum_val/cnt))