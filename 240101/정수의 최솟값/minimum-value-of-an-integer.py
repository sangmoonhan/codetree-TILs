def min(a, b, c):
    if a <= b and a <= c :
        return a
    elif b <= a and b <= c :
        return b
    elif c <= a and c <= b :
        return c

a, b, c = tuple(map(int,input().split()))


print(min(a,b,c))