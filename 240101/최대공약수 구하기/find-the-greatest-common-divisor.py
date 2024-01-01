def game(n,m):

    if n < m :
        a = n
    else :
        a = m

    num = 1
    
    for i in range(2,a+1):

        if n % i == 0 and m % i == 0 :
            num = i
    
    print(num)

n, m = tuple(map(int,input().split()))

game(n,m)