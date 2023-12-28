arr =[]

while True :

    ch = input()

    if ch == '0':
        break
    else:
        arr.append(ch)

print(len(arr))

for i in arr[::2]:
    print(i)