ch = 65

n = int(input())

for i in range(n):
    for j in range(n):
        print(chr(ch),end="")
        ch +=1
    print()