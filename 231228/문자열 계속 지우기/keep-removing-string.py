a = input()

b = input()


while b in a :
    n = a.index(b)
    m = len(b)

    a = list(a)

    for i in range(n, n+m ) :
        a.pop(n)
    
    a = ''.join(a)

print(a)