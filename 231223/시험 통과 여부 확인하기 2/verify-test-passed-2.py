n = int(input())

pas = 0

for i in range(n):
    arr = list(map(int,input().split()))

    mean_val = sum(arr) / 4

    if mean_val > 60 :
        print('pass')
        pas += 1
    else :
        print('fail')
    

print(pas)