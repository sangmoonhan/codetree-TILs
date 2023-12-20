n = int(input())

pn = "P"

for i in range(2,n):
    if n % i == 0 :
        pn = "C"

print(pn)