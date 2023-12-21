n = int(input())

for i in range(n):
    if i % 2 == 0 :
        for j in range(int(1 + (i / 2))):
            print("*", end=" ")
        print()
    else : 
        for j in range(int(n - (i-1)/2)):
            print("*", end=" ")
        print()

for i in range(n):
    if i % 2 == 0 :
        for j in range(int( (n+1)/2 - i/2 )):
            print("*", end=" ")
        print()
    else : 
        for j in range(int( n + (i-3)/2 )):
            print("*", end=" ")
        print()