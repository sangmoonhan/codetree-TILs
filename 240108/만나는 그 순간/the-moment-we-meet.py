n, m = tuple(map(int,input().split()))

arr, brr = [], []

t = 0

for _ in range(n):

    a = input().split()

    arr.append([a[0],int(a[1])])

    t += int(a[1])

for _ in range(m):

    b = input().split()

    brr.append([b[0],int(b[1])])

A, B = [0] * (t+1), [0] * (t+1) 

crr_a, crr_b = 0, 0

lo = 1
for i in range(n):
    
    d, num = arr[i][0], arr[i][1]

    while num : 
        if d == "R":
            crr_a += 1
        else:
            crr_a -= 1

        num -= 1
        A[lo] = crr_a
        lo += 1

lo = 1
for i in range(m):
    
    d, num = brr[i][0], brr[i][1]

    while num : 
        if d == "R":
            crr_b += 1
        else:
            crr_b -= 1
            
        num -= 1
        B[lo] = crr_b
        lo += 1

for i in range(1,len(A)):
    if A[i] == B[i]:
        print(i)
        break