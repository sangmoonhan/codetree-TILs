arr = list(map(int,input().split()))

n1, n2 = arr[0], arr[1]

A = list(map(int,input().split()))
B = list(map(int,input().split()))

jud = "No"

if B in A :
    print("Yes")
else : 
    print("No")