ch = input()

c = input()

result = -1

for i in range(0, len(ch)-len(c) + 2 ) :
    if c == ch[i:(i+len(c))] :
        print(i)
        result=0
        break

if result == -1 :
    print(-1)