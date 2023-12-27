ch = input()

ch = list(ch)

a = ch[0]
b = ch[1]

arr = [ 0 for i in range(len(ch))]
brr = [ 0 for i in range(len(ch))]

for i in range(len(ch)) :
    if ch[i] == a :
        arr[i] = 1
    
    if ch[i] == b :
        brr[i] = 1

for i in range(len(arr)) :
    if arr[i] == 1 :
        ch[i] = b

for i in range(len(arr)) :
    if brr[i] == 1 :
        ch[i] = a

ch = ''.join(ch)

print(ch)