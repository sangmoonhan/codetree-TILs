n = int(input())
ch=65
for i in range(n):
    for j in range(n):
        if j>=i :
            print(chr(ch), end=" ")
            if ch == 90 :
                ch = 65
            else :
                ch += 1
        else :
            print(" ",end=" ")
    print()