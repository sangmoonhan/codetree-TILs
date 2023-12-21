n = int(input())

cnt = 1 

for i in range(n):
    for j in range(n):
        if cnt == 9 :
            print(cnt,end="")
            cnt =1
        else : 
            print(cnt,end="")
            cnt = cnt + 1
    print()