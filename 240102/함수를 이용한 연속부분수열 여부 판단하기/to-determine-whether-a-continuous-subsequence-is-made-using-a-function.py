n, m = tuple(map(int,input().split()))

a = list(map(int,input().split()))
b = list(map(int,input().split()))

def is_sub(a,b):

    n = len(a)
    m = len(b)

    for i in range(n-m+1):
        cnt = 0
        for j in range(m):
            if b[j] == a[i+j]:
                cnt += 1
        
        if cnt == m :
            return True
    
    return False

if is_sub(a,b):
    print("Yes")
else :
    print("No")