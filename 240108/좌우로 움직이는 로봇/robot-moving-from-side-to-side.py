n, m = tuple(map(int,input().split()))

arr, brr = [], []

t1 = 0

for _ in range(n):

    a = input().split()

    arr.append([int(a[0]),a[1]])

    t1 += int(a[0])

t2 = 0

for _ in range(m):

    b = input().split()

    brr.append([int(b[0]),b[1]])

    t2 += int(b[0])

mt = max(t1,t2)

A, B = [0] * (t1+1), [0] * (t2+1) 

crr_a, crr_b = 0, 0

lo = 1
for i in range(n):
    
    t, d = tuple(arr[i])

    for _ in range(t):
        if d == "R":
            crr_a += 1
        else:
            crr_a -= 1
        
        A[lo] = crr_a
        lo += 1

lo = 1
for i in range(m):
    
    t, d = tuple(brr[i])

    for _ in range(t):
        if d == "R":
            crr_b += 1
        else:
            crr_b -= 1
        
        B[lo] = crr_b
        lo += 1

if mt == t1 :
    B += [crr_b] * (t1-t2)
else:
     
    A += [crr_a] * (t2-t1)

cnt = 0
for i in range(1,mt+1):

    jud = (A[i] == B[i])

    if i >= 2 :
        if jud == True and jud1 == False:
            cnt +=1
    
    jud1 = jud


print(cnt)