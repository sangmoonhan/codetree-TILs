ch = input()

n = int(input())

if n > len(ch):
    print(ch)
elif n == len(ch) :
    print(ch) 
else:
    for i in range(n):
        print(ch[-1-i],end="")