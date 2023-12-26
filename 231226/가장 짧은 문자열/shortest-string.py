a=len(input())
b=len(input())
c=len(input())

if a <= b and a <= c :
    min_val = a
elif b <= a and b <= c :
    min_val = b
else : 
    min_val = c

if b <= a and c <= a :
    max_val = a
elif a <= b and c <= b :
    max_val = b
else : 
    max_val = c

print(int( max_val - min_val ))