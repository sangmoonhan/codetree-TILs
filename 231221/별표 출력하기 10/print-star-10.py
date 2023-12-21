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

''' 5일때 3 6일때 4'''

if n & 2 == 0 :
    for i in range(n) :
        if i % 2 == 0:
            for j in range(int((n+1)/2 - i/2)):
                print("*",end=" ")
            print()
        else : 
            for j in range(int((n+1)/2 + (i+1)/2 )):
                print("*",end=" ")
            print()
else :
    for i in range(n) :
        if i % 2 == 0:
            for j in range(int(n/2 + 1 + i/2)):
                print("*",end=" ")
            print()
        else : 
            for j in range(int(n/2 - (i-1)/2 )):
                print("*",end=" ")
            print()