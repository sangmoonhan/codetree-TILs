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

for i in range(1,len(arr),2):
    arr[i] = str(arr[i])

sum_val = 0

for i in arr:
    sum_val += len(i)

print(sum_val)


for i in arr:
    print(i,end="")