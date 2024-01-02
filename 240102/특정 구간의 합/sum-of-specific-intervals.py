n, m = tuple(map(int,input().split()))

arr = list(map(int,input().split()))

def game(arr,m):

    for _ in range(m):

        a, b = tuple(map(int,input().split()))

        sum_val = 0

        for i in range(a-1,b):
            sum_val += arr[i]
        
        print(sum_val)

game(arr,m)