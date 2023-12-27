ch = input()

ch = list(ch)

a = ch[0]
b = ch[1]

for i in range(len(ch)):
    if ch[i] == b :
        ch[i] = a

print(''.join(ch))