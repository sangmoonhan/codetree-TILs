arr = list(map(int,input().split()))

n1, n2 = arr[0], arr[1]

A = list(map(int,input().split()))
B = list(map(int,input().split()))

jud = "No"

for i in range(n1 - n2 + 1) : 

    cnt = 0

    for j in range(i, i+n2):
        if A[j] == B[j-i]:
            cnt += 1
    
    if cnt == n2 :
        jud = "Yes" 

print(jud)