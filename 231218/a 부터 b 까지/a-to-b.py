arr = input().split()
a = int(arr[0])
b = int(arr[1])

while a <= b :
    if a == b :
        print(a, end=" ")
        a +=1
    elif a % 2 == 1 :
        print(a,end=" ")
        a *= 2
    elif a % 2 == 0 :
        print(a,end=" ")
        a += 3