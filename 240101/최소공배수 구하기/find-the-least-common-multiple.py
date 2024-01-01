def game(n,m):

    a = n*m

    num = 1

    for i in range(1,a+1):

        if i % n == 0 and i % m == 0 :
            num= i
            break
    
    print(num)

n, m = tuple(map(int,input().split()))

game(n,m)