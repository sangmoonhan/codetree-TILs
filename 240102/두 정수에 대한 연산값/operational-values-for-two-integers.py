def change(a,b):
    if a > b :
        a += 25
        b *= 2
    else :
        b += 25
        a *= 2
    
    return a, b

a, b = tuple(map(int,input().split()))

a,b = change(a,b)

print(a,b)