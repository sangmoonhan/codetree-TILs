''' A는 65 Z'''
n = int(input())
ch=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end="")
        if ch == 90 :
            ch = 65
        else:
            ch += 1
    print()