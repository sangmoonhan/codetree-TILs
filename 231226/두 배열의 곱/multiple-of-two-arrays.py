arr = [ list(map(int,input().split())) for i in range(3) ]

emp = input()

brr = [ list(map(int,input().split())) for i in range(3) ]

crr = [ [ 0 for j in range(3 )] for i in range(3) ]

for i in range(3):
    for j in range(3):
        crr[i][j] = arr[i][j] * brr[i][j]

        print(crr[i][j], end=" ")
    print()