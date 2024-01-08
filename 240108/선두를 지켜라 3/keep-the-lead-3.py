n, m = tuple(map(int,input().split()))

arr, brr = [], []

t = 0

for _ in range(n):

    a = list(map(int,input().split()))

    arr.append(a)

    t += int(a[1])

for _ in range(m):

    b = list(map(int,input().split()))

    brr.append(b)

A, B = [0] * (t+1), [0] * (t+1) 

cnts = [0] * (t+1)

crr_a, crr_b = 0, 0

lo = 1
for i in range(n):
    
    sp, t = tuple(arr[i])

    for _ in range(t):
        crr_a += sp
        A[lo] = crr_a
        lo += 1

lo = 1

for i in range(m):
    
    sp, t = tuple(brr[i])

    for _ in range(t):
        crr_b += sp
        B[lo] = crr_b
        lo += 1

# cnts = [0] * (t+1) 위에서 함

for i in range(1,len(A)):
    
    if A[i] > B[i]:
        cnts[i] = 1
    elif A[i] < B[i]:
        cnts[i] = 0
    else :
        cnts[i] = 2

cnt = 0

for i in range(1,len(cnts)):

    a = cnts[i]

    if i == 1 :
        cnt += 1
        b = a
        continue
    
    if b != a :
        cnt += 1
    
    b = a
    
print(cnt)