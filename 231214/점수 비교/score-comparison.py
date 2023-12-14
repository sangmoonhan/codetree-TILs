arr1 = input().split()
arr2 = input().split()

e1 = int(arr1[0])
m1 = int(arr1[1])

e2 = int(arr2[0])
m2 = int(arr2[1])


if e1 > e2 and m1 > m2 :
    print(1)
else:
    print(0)