n = int(input())

for i in range(n):
    for j in range(n):
        print("({},{})".format(n-i,n-j), end=" ")
    print()