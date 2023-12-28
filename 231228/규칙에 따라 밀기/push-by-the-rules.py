ch = input()

lr = input()

for i in lr:

    if i == 'L' :
        ch = ch[1:] + ch[0]

    else :
        ch = ch[-1] + ch[:-1]
        
print(ch)