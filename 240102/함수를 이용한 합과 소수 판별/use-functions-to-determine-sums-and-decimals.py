a, b = tuple(map(int,input().split()))

def is_prime(n):
    for i in range(2,n) :
        if n % i == 0 :
            return False
        
    return True

def is_even(n):

    n = list(str(n))

    sum_val = 0

    for i in n:
        sum_val += int(i)
    
    if sum_val % 2 == 0:
        return True
    else : 
        return False
        
cnt = 0

for j in range(a,b+1):

    if is_prime(j) and is_even(j) :
        cnt += 1

print(cnt)