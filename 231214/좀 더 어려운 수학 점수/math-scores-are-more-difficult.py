arr1 = input().split()
arr2 = input().split()

m1 = int(arr1[0])
e1 = int(arr1[1])

m2 = int(arr2[0])
e2 = int(arr2[1])

if m1 > m2 :
    print("A")
elif m1 < m2 :
    print("B")
else : 
    if e1 > e2 :
        print("A")
    elif e1 < e2 :
        print("B")