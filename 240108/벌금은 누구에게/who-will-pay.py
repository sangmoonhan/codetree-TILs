n, m, k = tuple(map(int,input().split()))

student = [0] * (n+1)


bs = 0
for i in range(m):

    b = int(input())

    student[b] += 1

    if (i+1) >= k :
        for j in range(1,len(student)):
            if student[j] == k:
                bs = j
                break
    
    if bs :
        print(bs)
        break

if bs == 0 :
    print(-1)