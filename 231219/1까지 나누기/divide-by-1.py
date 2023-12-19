n = int(input())

cnt = 0

for i in range(1,5000):
    if n <= 1 :
        break
    
    n = n // i
    cnt +=1

print(cnt)