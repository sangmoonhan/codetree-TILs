n = int(input())
c = "N"

for i in range(2,n) :
    if n % i == 0 :
        c = "C"

print(c)