arr1 = input().split()
arr2 = input().split()

age1 = int(arr1[0])
sex1 = arr1[1]

age2 = int(arr2[0])
sex2 = arr2[1]

if (age1 >= 19 and sex1 == "M") or (age2 >= 19 and sex2 == "M") :
    print(1)
else : 
    print(0)