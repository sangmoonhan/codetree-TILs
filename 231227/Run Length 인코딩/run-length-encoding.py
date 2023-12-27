ch = input()

arr = [ ch[0], 1]

cnt = 1

for i in range(1,len(ch)):
    if ch[i-1] == ch[i]:
        arr[cnt] += 1
    else :
        arr.append(ch[i])
        arr.append(1)
        cnt += 2

print(len(arr))

for i in arr:
    print(i,end="")