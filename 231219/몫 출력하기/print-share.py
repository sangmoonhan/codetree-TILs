cnt = 0

while True :
    n = int(input())

    if n % 2 == 1:
        continue
    if n % 2 == 0:
        n = n//2
        print(n)
        cnt += 1
    
    if cnt ==3 :
        break