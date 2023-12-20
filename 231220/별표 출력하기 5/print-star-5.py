n = int(input())

for i in range(1,n+1) :
    
    for j in range(n + 1 - i) :
        for k in range(n + 1 - i) : 
            print("*",end="")
        print("",end=" ")
    print()