arr = input().split()

ch = arr[0]
q = int(arr[1])

for _ in range(q):

    n = int(input())

    if n == 1 :
        ch = ch[1:] + ch[0]
        print(ch)
    elif n == 2 :
        ch = ch[-1] + ch[:-1]
        print(ch)
    else :
        ch = ch[::-1]
        print(ch)