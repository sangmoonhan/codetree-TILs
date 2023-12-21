n = int(input())

cnt =0

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            cnt += 1
            print(cnt,end=" ")
        cnt += n
    else: 
        for j in range(n):
            
            print(cnt,end=" ")
            cnt -= 1
        cnt += n
    print()