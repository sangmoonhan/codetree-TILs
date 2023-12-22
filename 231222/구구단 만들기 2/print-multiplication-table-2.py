arr = input().split()

a = int(arr[0])
b = int(arr[1])


for i in range(1,5):
    for j in range(int(b-a+1)) :
        print("{} * {} = {}".format(b-j, 2*i , 2*i * (b-j)  ), end= " ")
        if j < b-a :
            print("/",end=" ")
    print()