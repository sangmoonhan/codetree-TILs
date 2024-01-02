def change(a,b):
    if a > b :
        a *= 2
        b += 10
    else :
        b *= 2
        a += 10
    
    return a, b

a, b = tuple(map(int,input().split()))

a,b = change(a,b)

print(a,b)