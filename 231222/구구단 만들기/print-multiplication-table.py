arr = input().split()

a = int(arr[0])
b = int(arr[1])

cnt = 1

for i in range(9):
    for j in range(int((b-a)/2 + 1)) :
        print("{} * {} = {}".format(b-2*j, cnt, cnt * (b-2*j)  ), end= " ")
        if j < int((b-a)/2) :
            print("/",end=" ")
    cnt += 1
    print()