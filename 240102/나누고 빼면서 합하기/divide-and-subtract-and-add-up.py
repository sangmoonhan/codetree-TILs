n, m = tuple(map(int,input().split()))

arr = list(map(int,input().split()))

def game(arr,m):

    sum_val = 0

    c = m

    while c > 0 :
        
        sum_val += arr[c-1]
        
        if c % 2 == 0:
            c = c//2
        else :
            c -= 1
    
    return sum_val

print(game(arr,m))