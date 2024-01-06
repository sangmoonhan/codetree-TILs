a,b,c = tuple(map(int,input().split()))

d =  (a - 12) * 24 * 60
h = (24 + b - 12) * 60
m = 60 + c - 11

print(d + h + m)