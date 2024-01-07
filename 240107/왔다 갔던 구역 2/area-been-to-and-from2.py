n = int(input())

lo = 1500

arr = [0] * 3000

for j in range(n):

    brr = input().split() 

    x, d = int(brr[0]), brr[1]

    if j == 0:
        arr[lo] += 1

    if j >= 1:
        if d != d1 :
            arr[lo] += 1

    if d == "R" :

        for i in range(x):
            lo += 1
            arr[lo] += 1
    else :
        for i in range(x):
            lo -= 1
            arr[lo] += 1
    
    d1 = d

cnts = []

cnt = 0

for a in arr :

    if a >= 2 :

        cnt += 1
    else : 

        cnts.append(cnt-1)

        cnt = 0
    
sum_val = 0

for i in cnts :
    if i >= 1 :
        sum_val += i

print(sum_val)